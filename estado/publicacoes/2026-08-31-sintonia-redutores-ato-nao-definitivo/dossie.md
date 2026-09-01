# Dossiê — 2026-08-31

Janela: 26/08/2026 a 31/08/2026.
Pré-voo: `MODO=COMPLETO` (gov.br, cgibs.gov.br, cfc.org.br e toda a imprensa OK;
planalto.gov.br, www.in.gov.br, STF, STJ e CONFAZ bloqueados).

**Achado do pré-voo, para corrigir no script:** `www.in.gov.br` está bloqueado,
mas **`in.gov.br` (sem o `www`) responde e serve o DOU inteiro**. Foi por ele que
a fonte primária desta execução foi aberta. O `bin/preflight.sh` deveria testar
o host sem `www`, senão declara o DOU inacessível quando ele está acessível.

Orçamento de busca: 6 `WebSearch` (esgotado), 8 `WebFetch`, mais consultas
diretas ao índice do DOU via `curl`.

---

- titulo:        IN RFB nº 2.339/2026 altera o Programa Sintonia e cria redutores
                 de nota por lançamento não definitivo e por representação penal
  eixo:          tributario
  data:          2026-08-28 (publicação no DOU; ato de 21/08/2026)
  fonte_primaria: IN RFB nº 2.339, de 21/08/2026, DOU de 28/08/2026, Seção 1, p. 62.
                 Texto integral aberto e conferido em
                 https://in.gov.br/web/dou/-/instrucao-normativa-rfb-n-2.339-de-21-de-agosto-de-2026-728595216
                 Altera a IN RFB nº 2.316, de 25/03/2026 (ementa e data conferidas
                 no SIJUT/RFB), que dispõe sobre o Programa Sintonia instituído
                 pela LC nº 225, de 08/01/2026. Fundamentos invocados no próprio
                 preâmbulo: art. 7º, § 1º, III, da Lei nº 14.689/2023; art. 3º,
                 VI e XX, e art. 5º, II, da LC nº 225/2026.
  verificacao:   primaria
  o que faz:     (a) item 4.1.6 do Anexo Único: redutor de 0,05 no domínio
                 Consistência quando o contribuinte foi fiscalizado e o
                 procedimento se encerrou com constituição de crédito tributário,
                 ou quando houve despacho decisório com multa isolada do art. 18
                 da Lei nº 10.833/2003, para fatos a partir de 09/04/2026;
                 (b) item 4.1.6.1: o redutor é desconsiderado se revisão de ofício
                 ou julgamento administrativo resultar em nulidade do lançamento
                 ou em sua total improcedência;
                 (c) item 4.1.7: redutor de 0,2 se houver representação penal
                 formalizada no período;
                 (d) art. 6º, § 5º: esses redutores podem alcançar meses
                 posteriores ao mês de referência;
                 (e) art. 9º, § 4º: divulgação de nova classificação fora do prazo
                 ordinário, tanto para revisão julgada procedente (art. 17) quanto
                 para conclusão de procedimento fiscal que gere redutor;
                 (f) art. 10, §§ 1º e 2º: Selo Sintonia divulgado junto com a
                 classificação e válido por um ano a partir do 1º dia do mês
                 seguinte, independentemente da classificação no período,
                 ressalvado cancelamento de ofício do art. 15; revoga o § 5º;
                 (g) art. 14, §§ 3º a 5º: o benefício do inciso I do caput não se
                 aplica havendo indício de sonegação, fraude ou conluio (arts. 71
                 a 73 da Lei nº 4.502/1964), pedido de ressarcimento, restituição,
                 reembolso ou compensação com indício de falsidade (art. 18 da Lei
                 nº 10.833/2003) ou compensação com crédito do art. 74, § 12, II,
                 da Lei nº 9.430/1996; se a conduta não se confirmar, o direito é
                 restabelecido; aplica-se a procedimentos iniciados após
                 09/04/2026, desde que não cientificado o lançamento ou o despacho.
  repercussao:   Release da própria RFB em 28/08/2026 ("Receita Federal aperfeiçoa
                 Programa Sintonia"), sem cobertura própria em Conjur, Migalhas ou
                 JOTA até 31/08. Tema pouco disputado na rede: sinal de baixa
                 saturação, não de baixa relevância.
  angulo_copasul: a nota de conformidade passa a depender de eventos de
                 fiscalização e de despacho decisório, que chegam ao setor fiscal
                 por canais distintos dos da apuração (e-CAC, DTE) e com defasagem.

- titulo:        Nova edição da Malha Fiscal Digital para insuficiência de
                 declaração de PIS/Cofins, com prazo de autorregularização
  eixo:          tributario
  data:          2026-08-27
  fonte_primaria: Notícia da Receita Federal de 27/08/2026, aberta e conferida em
                 https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/agosto/receita-federal-oferece-oportunidade-de-regularizacao-de-divergencias-de-pis-e-cofins
                 (não há número de ato normativo; é ação administrativa)
  verificacao:   primaria
  o que faz:     divergências de R$ 300 milhões entre débitos declarados em DCTF e
                 valores apurados na EFD-Contribuições, alcançando mais de 3 mil
                 contribuintes (1.224 em São Paulo). Avisos por via postal, caixa
                 postal do e-CAC e, para maiores contribuintes, e-MAC. Prazo de
                 regularização até 30/10/2026; depois disso, fiscalização e auto de
                 infração com multa de ofício de 75% e juros de mora.
  repercussao:   apenas o release da RFB até 31/08.
  angulo_copasul: reconciliação DCTF x EFD-Contribuições é rotina de fechamento;
                 a malha transforma divergência de sistema em risco de 75%.

- titulo:        STF julgaria em 26/08 o voto de qualidade no CARF (ADIs 6399,
                 6403 e 6415) e em 28/08 o Tema 118 (ISS na base de PIS/Cofins,
                 RE 592.616)
  eixo:          tributario
  data:          2026-08-26 e 2026-08-28 (pauta anunciada)
  fonte_primaria: NÃO OBTIDA. portal.stf.jus.br respondeu 503/bloqueado no pré-voo
                 e no WebFetch. Só há notícia secundária de pauta, não de resultado.
  verificacao:   unica_secundaria
  descartado:    sim. `pesquisa.md`, modo degradado, regra 4: resultado de
                 julgamento, placar e trecho de voto não viram pauta sem a fonte.

- titulo:        Emenda Regimental STJ nº 48/2026, sobre conflitos entre entes e o
                 CGIBS relativos a IBS e CBS, concentrados na 1ª Seção
  eixo:          tributario
  data:          não confirmada (provavelmente anterior à janela)
  fonte_primaria: NÃO OBTIDA. www.stj.jus.br responde 403.
  verificacao:   unica_secundaria
  descartado:    sim. Sem data confirmada, não se prova que está na janela.

- titulo:        MP nº 1.386, de 24/08/2026, prorrogação excepcional dos prazos de
                 suspensão do drawback para compromissos afetados por tarifas
  eixo:          tributario
  data:          2026-08-24
  fonte_primaria: não aberta
  descartado:    sim. Fora da janela de 5 dias (24/08) e verificação insuficiente.

- titulo:        Direito Empresarial e Direito Contratual — janela vazia
  eixo:          empresarial / contratual
  data:          —
  fonte_primaria: —
  observacao:    duas buscas dedicadas (societário/recuperação/cooperativismo e
                 contratos/reequilíbrio/cláusula tributária), mais varredura da
                 capa do Migalhas de 26 a 31/08 e consulta ao índice do DOU, não
                 produziram fato normativo na janela. O que apareceu no eixo
                 contratual (arts. 374 e 375 da LC nº 214/2025 sobre reequilíbrio,
                 e o artigo do Conjur de 14/08) é anterior à janela e serve como
                 contexto, não como âncora.
