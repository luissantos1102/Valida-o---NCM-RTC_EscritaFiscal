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

- **2026-08-28 — 1ª edição de produção.** Modo: degradado (2/8 fontes
  primárias alcançáveis no pré-voo: gov.br e cgibs.gov.br OK; planalto.gov.br,
  in.gov.br, portal.stf.jus.br, stj.jus.br, confaz.fazenda.gov.br, cfc.org.br
  e valor.globo.com bloqueados). 2 itens, ambos em Direito Tributário: (1) RFB
  — Malha Fiscal Digital notifica 3.455 PJ por divergência de PIS/Cofins,
  R$ 299.090.225,86 em ajustes, prazo até 30/10/2026 (verificação primária,
  fonte aberta em gov.br); (2) CARF afasta IRPJ/CSLL sobre incentivo de ICMS
  do Fomentar/Produzir-GO, LC 160/2017 (verificação dupla_secundaria —
  Contábeis + Rota da Jurisprudência — número de acórdão não localizado).
  Reforma Tributária (IBS/CBS) e Contabilidade: 0 itens na janela de 24h —
  seções omitidas, não é dia sem novidade (há 2 itens no eixo Tributário).
  Um candidato sobre STF/CARF (fim do voto de qualidade) foi descartado por
  erro de data na fonte de cruzamento (matéria de 2022 confundida com 2026) —
  registrado no e-mail como aviso e no Radar como item a confirmar. E-mail
  enviado para luis.santos@copasul.coop.br, thread 1a047e917f5d0c36.

- **2026-08-28 11:47-11:48 UTC — auditoria e teste de layout (identidade
  Copasul).** Usuário apontou, na 1ª edição de produção: abuso de travessão
  no texto (tanto aqui quanto no carrossel do LinkedIn) e parágrafos
  alinhados à esquerda em vez de justificados. Também pediu mudança de
  layout só para a newsletter: paleta Copasul (verde #049444/#005E32/#014726,
  amarelo #FFDD21, cinzas #D9D9D9/#777777) no lugar do marinho/âmbar do
  LinkedIn; fonte Poppins; label "E na prática, o que muda para a Copasul"
  no lugar de "Por que importa"; cartão mais largo (660px → 840px, ~2,5cm a
  mais de cada lado). `template/email_newsletter.html`,
  `references/redacao.md`, `SKILL.md` e `bin/temas.py` (justify no carrossel)
  atualizados. Reenviado teste de layout na thread 1a048324a9d64987 (1º envio
  saiu quebrado por erro operacional meu — mandei `$(cat ...)` de shell em
  vez do conteúdo HTML lido; reenviado corrigido logo em seguida). Confirmado
  por leitura do HTML entregue: paleta/justify/label sobreviveram; a tag
  `<link>` do Google Fonts foi removida no envio (mesmo padrão do `<img>`),
  então a fonte real entregue é o fallback Arial, documentado no template.
  Usuário também perguntou por que o pré-voo está em modo degradado: rodado
  `bin/preflight.sh` de novo, confirma bloqueio total (http=000) de
  planalto.gov.br, in.gov.br, portal.stf.jus.br, confaz.fazenda.gov.br,
  cfc.org.br e valor.globo.com, e HTTP 403 de stj.jus.br — é a política de
  rede (allowlist) do ambiente de execução, não algo corrigível em código;
  correção fica a cargo do usuário na configuração do environment (Claude
  Code on the web).

- **2026-08-28 12:00-12:25 UTC — usuário adicionou os domínios ao ambiente e
  pediu 2ª rodada de auditoria visual.** Usuário confirmou ter adicionado a
  lista completa de domínios (PRIMARIAS + IMPRENSA) na configuração de rede
  dos dois ambientes (LinkedIn e Newsletter) — efeito só aparece em sessão
  nova, não nesta. Em seguida, mandou prints do sistema interno "Validador
  de Conformidade Fiscal" da Copasul (fundo cinza claro, barra verde no
  topo, cartão de conteúdo branco) como referência e pediu duas mudanças:
  (1) travessão passa de "no máximo 1 a cada 2-3 parágrafos" para **proibido,
  sem exceção** — atualizado em `references/redacao.md`, `SKILL.md` e
  `linkedin-pipeline/references/redacao.md` (mesma regra vale pro LinkedIn);
  (2) layout visual trocado de cartão escuro para o padrão sóbrio dos
  sistemas internos Copasul: fundo `#D9D9D9` sempre, cartão branco, barra
  verde `#014726` só no cabeçalho, amarelo `#FFDD21` restrito a realces
  pontuais e pequenos (nunca bloco grande nem texto corrido, contraste ruim
  em branco) — regra "mais escuro para mais volume, mais claro só para
  destaque" documentada no cabeçalho do template.
  `templates/email_newsletter.html` reescrito. Teste enviado na thread
  1a04854e75ff5bd6 com o mesmo conteúdo das rodadas anteriores, revisado
  para zero travessão (conferido com grep antes do envio) e confirmado
  entregue em tamanho completo (14,3 KB, sem o erro de shell da rodada
  anterior).

- **2026-08-28 12:32 UTC — 3ª rodada de ajuste visual, mesma auditoria.**
  Usuário corrigiu a 2ª versão: o CARTÃO em si (não só a página por trás)
  precisa estar em `#D9D9D9`, e o texto do corpo precisa de mais peso
  ("grossura") para dar corpo à leitura. Invertido o esquema: página agora
  branca, cartão cinza claro; caixas internas (aviso, fontes) viraram
  brancas para se destacar de dentro do cartão cinza; parágrafos de corpo
  ganharam `font-weight:600` (Arial só tem 400/700 reais, mas a maioria dos
  motores sintetiza traço mais grosso a partir de 600; documentado no
  template por que não usar 500). `templates/email_newsletter.html`
  reescrito de novo. Teste enviado na thread 1a0485b3b209b205, confirmado
  entregue em tamanho completo (13,6 KB).

- **2026-08-28 12:45 UTC — 4ª rodada, layout baseado em referência real da
  Copasul.** Usuário anexou um e-mail de verdade do setor de comunicação
  interna ("Pílula do Compliance: Relacionamento com Agentes Públicos") e
  pediu para seguir aquele layout. Extraído com `pdftotext`/leitura de PDF
  (foi preciso instalar `poppler-utils` via apt, ausente no ambiente).
  Elementos replicados em CSS puro (sem `<img>`, sem gradiente): cabeçalho
  com kicker + linha em itálico com os três eixos + título com a data, selo
  circular de destaque à direita; corpo de cada item movido para dentro de
  uma caixa `#014726` com texto quase branco (`#F2F5F8`) e o dado central
  de cada parágrafo em `<strong style="color:#FFDD21">`, replicando os
  termos-chave em amarelo do e-mail de referência ("Corrupção/Propina/
  Suborno"); sub-título "E na prática, o que muda para a Copasul" também em
  amarelo dentro da caixa; Radar virou faixa verde cheia (`#049444`) com
  texto branco, no lugar da lista simples; rodapé ganhou menção de marca em
  texto estilizado ("copasul · somos coop", nunca o logo de verdade, que é
  imagem e seria removida no envio). `templates/email_newsletter.html`,
  `references/redacao.md` e `SKILL.md` atualizados. Teste enviado na thread
  1a048674023be132, confirmado entregue em tamanho completo (15,4 KB).
