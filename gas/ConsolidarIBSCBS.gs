/**
 * Consolida os CSVs de uma pasta do Google Drive e envia os dados
 * já formatados para duas planilhas do Google Sheets.
 *
 * Tradução do script Python (Colab + gspread) equivalente para
 * Google Apps Script, para ser executado diretamente por um botão
 * na planilha (sem depender de autenticação externa via Colab).
 *
 * Configuração: veja instruções em gas/README.md.
 */

const ID_DA_PASTA = '1X5V_D3tOBc2ZwKCNb--9vWCt-7rY_iD4';

const ID_PLANILHA_1 = '1yVqAddAQtCtwF92tfg_OIRxm9hzieYR-sLhAzRmPjVk';
const NOME_ABA_1 = 'Base de dados (IBS/CBS)';

const ID_PLANILHA_2 = '19_tUvOhRQSOJ7RCAm_w7FSWTwobDZn-7BC_soNMne_w';
const NOME_ABA_2 = 'relatorio';

const COLUNAS_VALORES = [
  '[Item] Valor da CBS',
  '[Item] Valor do IBS de competência da UF',
  '[Item] Valor da Base de cálculo comum a IBS/CBS',
  'Valor total do IBS da UF',
  'Valor total da BC do IBS e da CBS',
  'Valor total da CBS'
];

/**
 * Cria o menu "Consolidação IBS/CBS" ao abrir a planilha, com um
 * atalho para rodar o processo sem precisar desenhar um botão.
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Consolidação IBS/CBS')
    .addItem('Atualizar dados agora', 'processarArquivosCSV')
    .addToUi();
}

/**
 * Função principal, para ser atribuída a um botão desenhado na
 * planilha (Inserir > Desenho, depois "Atribuir script" apontando
 * para "processarArquivosCSV").
 */
function processarArquivosCSV() {
  const ui = SpreadsheetApp.getUi();
  try {
    Logger.log('Iniciando o processo...');
    Logger.log('Procurando os arquivos na pasta do Drive...');

    const pasta = DriveApp.getFolderById(ID_DA_PASTA);
    const iteradorArquivos = pasta.getFiles();
    const arquivos = [];
    while (iteradorArquivos.hasNext()) {
      arquivos.push(iteradorArquivos.next());
    }

    if (arquivos.length === 0) {
      ui.alert('Nenhum arquivo encontrado dentro dessa pasta. Verifique se eles estão lá.');
      return;
    }

    Logger.log(`Foram encontrados ${arquivos.length} arquivo(s). Lendo e juntando os dados...`);

    const tabelas = arquivos.map(function (arquivo) {
      Logger.log('  -> Lendo o arquivo: ' + arquivo.getName());
      const conteudo = arquivo.getBlob().getDataAsString('UTF-8');
      const linhas = Utilities.parseCsv(conteudo, ',');
      const cabecalho = linhas[0] || [];
      const dados = linhas.slice(1);
      return { cabecalho: cabecalho, dados: dados };
    });

    // Une as colunas de todos os arquivos preservando a ordem de
    // primeira aparição, igual ao comportamento do pd.concat.
    const colunasUnificadas = [];
    const indiceDaColuna = {};
    tabelas.forEach(function (tabela) {
      tabela.cabecalho.forEach(function (coluna) {
        if (!(coluna in indiceDaColuna)) {
          indiceDaColuna[coluna] = colunasUnificadas.length;
          colunasUnificadas.push(coluna);
        }
      });
    });

    // Realinha as linhas de cada arquivo pela coluna unificada,
    // preenchendo com "" onde o arquivo não tem aquela coluna.
    let linhasFinais = [];
    tabelas.forEach(function (tabela) {
      const mapaColuna = tabela.cabecalho.map(function (coluna) {
        return indiceDaColuna[coluna];
      });
      tabela.dados.forEach(function (linha) {
        const novaLinha = new Array(colunasUnificadas.length).fill('');
        linha.forEach(function (valor, i) {
          novaLinha[mapaColuna[i]] = valor;
        });
        linhasFinais.push(novaLinha);
      });
    });

    Logger.log('Formatando as colunas financeiras...');
    const indicesValores = COLUNAS_VALORES
      .map(function (coluna) {
        return indiceDaColuna[coluna];
      })
      .filter(function (indice) {
        return indice !== undefined;
      });

    linhasFinais.forEach(function (linha) {
      indicesValores.forEach(function (indice) {
        linha[indice] = formatarValorMonetario(linha[indice]);
      });
    });

    const dadosParaEnviar = [colunasUnificadas].concat(linhasFinais);

    Logger.log('Conectando à PRIMEIRA planilha do Google Sheets...');
    enviarParaPlanilha(ID_PLANILHA_1, NOME_ABA_1, dadosParaEnviar);

    Logger.log('Conectando à SEGUNDA planilha do Google Sheets...');
    enviarParaPlanilha(ID_PLANILHA_2, NOME_ABA_2, dadosParaEnviar);

    Logger.log('Processo concluído com sucesso! Ambas as planilhas foram atualizadas.');
    ui.alert('🎉 Processo concluído com sucesso! Ambas as planilhas foram atualizadas.');
  } catch (erro) {
    Logger.log('Erro: ' + erro.message);
    ui.alert('Ocorreu um erro: ' + erro.message);
    throw erro;
  }
}

/**
 * Replica a limpeza feita no pandas:
 * remove "R$", remove ponto de milhar, troca vírgula decimal por
 * ponto e converte para número. Valor vazio/ inválido vira "".
 */
function formatarValorMonetario(valor) {
  if (valor === null || valor === undefined) {
    return '';
  }
  let texto = String(valor).replace(/R\$/g, '').trim();
  if (texto === '') {
    return '';
  }
  texto = texto.replace(/\./g, '');
  texto = texto.replace(',', '.');
  const numero = parseFloat(texto);
  return isNaN(numero) ? '' : numero;
}

/**
 * Limpa a aba e escreve os dados a partir de A1, igual a
 * aba.clear() + aba.update(values=..., range_name='A1') no gspread.
 */
function enviarParaPlanilha(idPlanilha, nomeAba, dados) {
  const planilha = SpreadsheetApp.openById(idPlanilha);
  const aba = planilha.getSheetByName(nomeAba);
  if (!aba) {
    throw new Error('Aba "' + nomeAba + '" não encontrada na planilha ' + idPlanilha);
  }

  Logger.log('Limpando os dados antigos da aba "' + nomeAba + '"...');
  aba.clear();

  if (dados.length === 0 || dados[0].length === 0) {
    return;
  }

  Logger.log('Enviando os novos dados para a aba "' + nomeAba + '"...');
  aba.getRange(1, 1, dados.length, dados[0].length).setValues(dados);
}
