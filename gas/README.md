# Consolidação IBS/CBS — Google Apps Script

Tradução do script Python (Colab + gspread) para Google Apps Script (GAS),
para rodar direto de um botão na planilha, sem precisar do Colab.

O script faz exatamente o que o Python fazia:
1. Lista todos os CSVs dentro da pasta do Drive (`ID_DA_PASTA`).
2. Lê e junta todos eles (alinhando colunas pelo nome, como `pd.concat`).
3. Limpa as colunas financeiras (`R$`, ponto de milhar, vírgula decimal).
4. Limpa e reenvia os dados para as duas planilhas configuradas.

## Instalação

1. Abra a planilha onde o botão vai morar (pode ser a `ID_PLANILHA_1`, a
   `ID_PLANILHA_2`, ou uma planilha "painel de controle" separada — o
   script funciona em qualquer uma, pois ele abre as duas planilhas de
   destino pelo ID).
2. Menu **Extensões → Apps Script**.
3. Apague o conteúdo padrão de `Código.gs` e cole o conteúdo de
   [`ConsolidarIBSCBS.gs`](./ConsolidarIBSCBS.gs).
4. Salve o projeto (ícone de disquete).
5. Rode a função `processarArquivosCSV` uma vez pelo próprio editor
   (▶️ Executar) para autorizar o script a acessar Drive e Sheets. Na
   primeira execução o Google vai pedir permissão — aceite.

## Criando o botão na planilha

O Apps Script não cria "botões" nativos via código, então o botão é
desenhado manualmente e associado à função:

1. Na planilha, **Inserir → Desenho**.
2. Desenhe/escreva algo como "Atualizar dados" e clique em **Salvar e fechar**.
3. Clique no desenho recém-criado, depois nos três pontinhos (⋮) no
   canto superior direito dele → **Atribuir script**.
4. Digite exatamente: `processarArquivosCSV`
5. Pronto — clicar no desenho agora roda o processo inteiro.

Alternativa sem desenhar nada: ao reabrir a planilha (ou dar F5), vai
aparecer o menu **Consolidação IBS/CBS → Atualizar dados agora**, criado
pela função `onOpen()`.

## Configuração

No topo de `ConsolidarIBSCBS.gs`:

- `ID_DA_PASTA` — pasta do Drive com os CSVs.
- `ID_PLANILHA_1` / `NOME_ABA_1` — primeira planilha de destino.
- `ID_PLANILHA_2` / `NOME_ABA_2` — segunda planilha de destino.
- `COLUNAS_VALORES` — colunas que recebem a limpeza financeira.

## Diferenças em relação ao script Python

- Não precisa de `google.colab.auth` nem de credenciais externas: o
  Apps Script já roda com a identidade de quem clica no botão/menu,
  usando os escopos padrão de `DriveApp` e `SpreadsheetApp`.
- `print(...)` virou `Logger.log(...)` (visível em **Execuções**, no
  editor do Apps Script) e mensagens de erro/sucesso aparecem também
  em um alerta (`ui.alert`) na própria planilha.
- O separador do CSV continua sendo vírgula (`,`), igual ao Python
  (`sep=','`).
