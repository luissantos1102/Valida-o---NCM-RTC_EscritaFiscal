# Log — Newsletter Tributária

Registro de cada edição enviada: data/hora, quantidade de itens, eixos
cobertos, modo (completo/degradado). Ver `.claude/skills/newsletter-tributaria/SKILL.md`.

- **2026-08-28 01:41-01:52 UTC — rodada 1, 2 e 3 de teste visual** (não são
  edições de produção, thread separada, "[Teste de layout]" no assunto).
  Modo: degradado (2/8 fontes primárias alcançáveis no pré-voo). 5 itens: STF
  (Tema 1.455 IPTU), CARF (2 acórdãos), EFD-Reinf NT 04/2026, CFC (2 itens —
  NBC TSP 36 e Orientação 1/2026). Rodada 1 ficou superficial (rejeitada);
  rodada 2 corrigiu prosa/links/visual (aprovada como padrão, documentado em
  `references/redacao.md`); rodada 3 reenviou o mesmo conteúdo só para
  confirmar que banner/selos (assets reduzidos de tamanho) carregam no Gmail.
  `enviados.json` não foi atualizado com esses itens — são teste, não edição
  real; a primeira edição de produção (Routine de amanhã) começa o dedup do
  zero.

- **2026-08-28 02:00 UTC — rodada 4 (final) de teste visual.** Causa raiz
  encontrada: `mcp__Gmail__send_message` remove toda tag `<img>` do HTML
  antes de enviar (testado com link externo e com anexo inline via
  Content-ID — ambos removidos) e remove a propriedade CSS `background`
  (mas preserva `background-color`). Template, SKILL.md e redacao.md
  atualizados para nunca usar `<img>` e sempre `background-color`. Selos de
  seção agora são círculos em CSS puro. Confirmado por leitura do HTML
  entregue (get_thread): cartão escuro e os três círculos T/R/C sobreviveram
  intactos nesta rodada. Este é o padrão definitivo a partir de agora.
