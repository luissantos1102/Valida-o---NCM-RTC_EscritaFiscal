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

- **2026-08-28 13:00-13:20 UTC — layout definitivo (5ª rodada).** Usuário
  não gostou da 4ª rodada ("Não consegui gostar!"). Pesquisado na web
  referências reais de newsletter (editorial, "smart brevity" corporativo,
  cartão leve, memorando interno) e montada uma vitrine com quatro layouts
  completos, mesmo conteúdo real (RFB/CARF), publicada como artifact para o
  usuário escolher antes de qualquer envio. Usuário pediu uma 5ª opção:
  junção de "Editorial" (prosa em serifa, sem caixa) e "Cartão leve"
  (cartão arredondado com identidade Copasul discreta), com o fundo do
  cartão trocado de `#D9D9D9` para `#F9F9F9`. Adicionada essa 5ª opção à
  mesma vitrine; usuário aprovou e pediu para seguir com a fonte serifa.
  `templates/email_newsletter.html` reescrito com essa identidade
  definitiva: cartão `#F9F9F9`, corpo em Georgia (serifa nativa de e-mail,
  não depende de fonte web), item em prosa corrida sem caixa colorida,
  "E na prática..." como chamada em itálico dentro do parágrafo, selo
  pequeno (22px), amarelo restrito à régua fina de 3px sob o título, Radar
  de volta a lista simples. `references/redacao.md` e `SKILL.md`
  atualizados, com o histórico das rodadas 1 a 4 marcado como superado (não
  implementar de novo sem pedido explícito). Teste final enviado na thread
  1a0488736d991569, confirmado entregue em tamanho completo (13,5 KB). Este
  é o padrão de produção a partir de agora.

- **2026-08-28 13:46 UTC — ajuste do cabeçalho.** Logo após aprovar o
  layout definitivo, usuário pediu que só o cabeçalho ganhasse fundo verde
  mais escuro (`#014726`), título grande em branco e detalhes (kicker,
  subtítulo) em amarelo. Aplicado apenas no bloco do cabeçalho; o resto do
  cartão continua `#F9F9F9` sem fundo colorido. `templates/email_newsletter.html`
  e `references/redacao.md` atualizados. Teste enviado na thread
  1a0489f45f6db51b, confirmado entregue em tamanho completo (7,9 KB).

- **2026-08-28 17:09 UTC — execução agendada, sem envio (invariante "um
  e-mail por dia").** Rotina disparou pedindo a edição de hoje, mas a
  varredura deste log mostra que a 1ª edição de produção do dia já havia
  sido enviada (thread `1a047e917f5d0c36`, itens já registrados em
  `enviados.json` com `enviado_em: 2026-08-28`), e o relógio do sistema
  confirma que ainda é 2026-08-28 (17:09 UTC), mesmo dia calendário. Como o
  invariante da skill veda expressamente uma segunda edição no mesmo dia,
  esta execução não gerou pesquisa nem novo e-mail; nenhuma alteração em
  `enviados.json`. Próximo disparo da rotina deve produzir a edição de
  amanhã normalmente.

- **2026-08-28 (fim de tarde) — 6ª geração de layout: verde Copasul sobre a
  edição real.** Usuário anexou o PDF da própria 1ª edição de produção do
  dia (enviada de manhã, thread `1a047e917f5d0c36`, ainda no template
  marinho/âmbar herdado do LinkedIn) e pediu duas versões idênticas, só
  trocando o azul do fundo do cartão por verde: `#184B44` e `#013220`.
  Montada uma vitrine (artifact) com as duas réplicas; usuário escolheu
  `#013220`. Rodadas seguintes de ajuste, todas no mesmo dia: fonte
  Arial (com a exceção do título do cabeçalho, mantido em Georgia a
  pedido), "E na prática, o que muda para a Copasul" virou linha própria
  em caixa alta e negrito, zero travessão (reescrita de todo o texto
  herdado do e-mail original, que tinha vários), painéis internos trocados
  do azul original para verde V3 (`#1B5E42`/borda `#2F8C63`, entre 4
  opções apresentadas), destaques de dado-chave restaurados em âmbar
  (tinham se perdido na reescrita sem travessão), título de eixo maior
  (12px → 17px), cartão alargado de 660px para 890px, texto justificado,
  cor do corpo trocada de cinza apagado (`#A9BACB`) para quase-branco
  (`#F2F5F8`), título do cabeçalho com os nomes por extenso
  ("Direito Tributário · Reforma Tributária · Contabilidade") reduzido
  para caber em uma linha. Na revisão por e-mail, usuário reportou cores
  "muito diferentes"; investigado via `get_thread` e descoberta a causa
  real: o Gmail autolinkifica menções de domínio em texto puro (ex.:
  "planalto.gov.br") com o azul padrão dele, ilegível sobre fundo escuro,
  mesmo com o HTML enviado batendo 100% com o template. Corrigido
  transformando toda menção de domínio em `<a href>` real com
  `color:#D6A544` explícito. Testes finais enviados nas threads
  `1a049ba5e84fa118` e `1a049bfcc4a2bf07` (esta última já com os links
  corrigidos), ambos confirmados entregues em tamanho completo (~22 KB).
  **`templates/email_newsletter.html` foi reescrito do zero** para essa
  6ª geração (a versão anterior, cartão `#F9F9F9` em serifa, nunca tinha
  sido portada do rascunho de teste pro arquivo real do projeto — só
  existia nos artifacts da conversa). `references/redacao.md` e
  `SKILL.md` atualizados. Este é o padrão de produção a partir de agora.

- **2026-08-29 10:56 UTC — 2ª edição de produção.** Modo: completo (3/8
  fontes primárias alcançáveis no pré-voo: gov.br, cgibs.gov.br e
  cfc.org.br OK; planalto.gov.br, in.gov.br, portal.stf.jus.br,
  confaz.fazenda.gov.br bloqueados com http=000, stj.jus.br com HTTP 403;
  imprensa especializada 100% alcançável). 2 itens, ambos em Direito
  Tributário: (1) IN RFB 2.339/2026, que altera a IN RFB 2.316/2026 e
  ajusta o domínio "Consistência" do Programa Sintonia (verificação
  primária, fonte aberta em gov.br); (2) LC 235/2026, que reduz tributos
  federais sobre combustíveis e cria subsídio para etanol e crédito para
  fertilizantes, em resposta ao choque de preços do conflito no Oriente
  Médio (verificação dupla_secundaria: planalto.gov.br/in.gov.br
  inacessíveis nesta sessão, número e termos confirmados de forma cruzada
  em notas do Senado e da Câmara, com reforço de imprensa; e-mail traz
  ressalva de verificação explícita no item e no radar). Reforma
  Tributária (IBS/CBS) e Contabilidade: 0 itens na janela de 24h, seções
  omitidas. Layout: template verde Copasul (6ª geração) do dia anterior
  usado sem alterações. E-mail enviado para luis.santos@copasul.coop.br,
  thread `1a04d29c64c1b33c`, confirmado entregue em tamanho completo
  (21,3 KB) via `get_thread`.

- **2026-08-30 12:25 UTC — 3ª edição de produção, "dia sem novidade".**
  Pré-voo: `MODO=COMPLETO` (limiar `ok_p>=3`; na prática só 3/8 fontes
  primárias alcançáveis: gov.br, cgibs.gov.br, cfc.org.br OK; planalto.gov.br,
  in.gov.br, portal.stf.jus.br, stj.jus.br e confaz.fazenda.gov.br
  bloqueados). Pesquisa delegada ao agente `pesquisador-fiscal`: 29 e
  30/08/2026 caíram em sábado e domingo, sem publicação no DOU nem ato novo
  de RFB, CARF ou CFC nas últimas 24h, confirmado por varredura direta das
  páginas de notícias de cada órgão. Os achados mais recentes localizados
  (27 e 28/08) já constavam em `enviados.json` (RFB/Malha Fiscal PIS-Cofins,
  CARF/Fomentar-GO, IN RFB 2.339/2026, LC 235/2026) ou ficaram fora da
  janela de 24h. Nenhum item novo verificável nos três eixos: seguiu a
  seção "Dia sem novidade" da skill, sem forçar pauta. `enviados.json` não
  foi alterado nesta edição (nenhum item novo a registrar; as entradas
  existentes seguem dentro dos 7 dias). E-mail curto enviado, com um
  parágrafo de contexto e Radar com 3 itens pendentes de desdobramento
  (PLP 108/2024 no Senado, efeitos práticos do julgamento do STF de 26/08
  sobre voto de qualidade no CARF, debate do modelo do Simples Nacional
  2027 híbrido/puro). Bloqueio adicional identificado pelo agente, fora da
  lista do preflight: `www.camara.leg.br` (EGRESS_BLOCKED); e as
  ferramentas `mcp__Jusratio__pesquisar_documentos` e
  `mcp__Jusratio__informativo_juridico` não estavam registradas nesta
  sessão, limitando a cobertura independente de STF/STJ. E-mail enviado
  para luis.santos@copasul.coop.br, thread `1a052a17f36d4606`, confirmado
  entregue em tamanho completo (5,6 KB) via `get_thread`.

- **2026-08-31 14:15 UTC — 4ª edição de produção, "dia sem novidade".**
  Pré-voo: `MODO=COMPLETO` (3/8 fontes primárias alcançáveis: gov.br,
  cgibs.gov.br, cfc.org.br OK; planalto.gov.br, in.gov.br, portal.stf.jus.br
  e confaz.fazenda.gov.br bloqueados com http=000, stj.jus.br com HTTP 403;
  toda a imprensa especializada acessível). Pesquisa delegada ao agente
  `pesquisador-fiscal`: nenhum fato normativo novo nos três eixos na janela
  de 24h (30 a 31/08). Achados reais localizados ficaram fora da janela
  (ADE CORAT 63/2026 de 26/08, Soluções de Consulta RFB 154 e 155 de 20/08,
  Resolução CGSN 186/2026 e julgamento do STF sobre voto de qualidade no
  CARF, ambos de 26/08, sem desdobramento novo) ou eram apenas prazos de
  agenda recorrente (vencimentos de 31/08 já previstos em norma
  preexistente). Confirmado também que o item de radar "PLP 108/2024 no
  Senado" estava desatualizado: o projeto já virou LC 227/2026 há meses,
  sem tramitação nova a reportar. `mcp__Jusratio__pesquisar_documentos` e
  `mcp__Jusratio__informativo_juridico` não estavam registrados nesta
  sessão; `valor.globo.com` e `jota.info` não serviram como fonte
  confiável via WebFetch (falha de rede e conteúdo carregado via JS,
  respectivamente), sem impacto no resultado porque não havia achado a
  confirmar por essas vias. Seguiu a seção "Dia sem novidade" da skill,
  sem forçar pauta; `enviados.json` não foi alterado (nenhum item novo;
  entradas existentes seguem dentro dos 7 dias). E-mail curto enviado com
  um parágrafo de contexto e Radar com 3 itens atualizados (janela do
  Simples Nacional 2027 híbrido/puro em setembro, acórdão pendente do STF
  sobre voto de qualidade no CARF, agenda tributária de setembro via ADE
  CORAT 63/2026). E-mail enviado para luis.santos@copasul.coop.br, thread
  `1a0582ca33b9176f`, confirmado entregue em tamanho completo (5,5 KB) via
  `get_thread`.

- **2026-09-01 14:21 UTC — 5ª edição de produção, 2 itens.** Pré-voo:
  `MODO=COMPLETO` (3/8 fontes primárias alcançáveis: gov.br, cgibs.gov.br,
  cfc.org.br OK; planalto.gov.br, in.gov.br, portal.stf.jus.br,
  confaz.fazenda.gov.br bloqueados com http=000, stj.jus.br com HTTP 403;
  imprensa especializada toda acessível). Push de estado testado e
  confirmado funcional nesta sessão (o `git push --dry-run` do preflight
  tinha acusado bloqueio só porque o branch local estava atrás do remoto
  por 11 commits; após `git pull --ff-only` o push funcionou normalmente,
  sem falso positivo real de credencial). Pesquisa delegada ao agente
  `pesquisador-fiscal` (ferramentas `mcp__Jusratio__*` não registradas
  nesta sessão): nenhuma norma nova publicada nas últimas 24h nos três
  eixos, mas dois fatos com consequência jurídica hoje (prazo/vigência que
  começa), verificados por dupla fonte secundária independente cada um,
  já que as páginas específicas de notícia no domínio gov.br não
  renderizaram via WebFetch nesta execução (falha pontual, não bloqueio de
  domínio): (1) IN RFB 2.332/2026 (monitoramento contínuo de benefícios
  fiscais de PJ, EC 109/2021 e art. 43 §2º da Lei 14.973/2024) entra em
  vigor hoje, eixo tributário; (2)
  Resolução CGSN 186/2026 abre hoje, até 30/09/2026, a janela de opção
  pelo regime regular de IBS/CBS para 2027 no Simples Nacional, eixo
  reforma.
  Eixo contabilidade: 0 achados (item mais próximo, Resolução CVM 244/2026
  sobre relatório de sustentabilidade ISSB, fora da janela de 24h).
  Bloqueios de egress adicionais identificados pelo agente, fora da lista
  do preflight: taxesbrasil.com.br, www.legisweb.com.br, crcmg.org.br,
  dtadvogados.com.br, reformatributaria360.com.br,
  www.reformatributaria.com, www12.senado.leg.br (todos EGRESS_BLOCKED,
  não erro transitório). `enviados.json` atualizado com os 2 itens novos;
  entradas de 27-28/08 mantidas (dentro dos 7 dias). Falha operacional:
  o primeiro envio (`mcp__Gmail__send_message`, thread `1a05d56163c38164`)
  saiu com o corpo HTML substituído por engano por um placeholder literal
  (`<LOAD_FROM_FILE>`, 838 bytes) em vez do conteúdo real, por erro do
  operador ao montar a chamada da ferramenta. Detectado imediatamente por
  `get_thread`. Corrigido no mesmo turno com um segundo envio na mesma
  thread (`replyThreadId`), com nota de correção no topo do e-mail
  avisando que a mensagem anterior falhou e essa a substitui, contendo a
  edição completa (22,2 KB), confirmado entregue via `get_thread`. Não
  conta como segunda edição do dia: é a correção de uma falha técnica de
  envio da mesma execução, ambas na mesma thread.

- **2026-09-01 17:19-17:24 UTC — teste do fluxo de distribuição
  (`newsletter-aprovacao`).** Primeiro ciclo real: usuário pediu, em
  conversa, a etapa de decisão para mandar a newsletter também à equipe
  (escritafiscal.centralizada@copasul.coop.br), condicionada a ele
  responder "ENVIAR" na thread do dia. Ciclo criado retroativamente para a
  edição de hoje (que já tinha saído antes da mudança existir), com
  `destino_override` para o e-mail pessoal do usuário só para este teste.
  Usuário respondeu "ENVIAR" às 17:19 UTC (classificação inequívoca).
  Encaminhamento não foi usado por pedido explícito do usuário ("não quero
  um fwd") — o envio foi feito como mensagem nova via
  `mcp__Gmail__send_message`, mesmo assunto, sem citar a thread original,
  usando o HTML salvo em
  `estado/newsletter/aprovacoes/2026-09-01/newsletter.html`. Entregue às
  17:24 UTC (thread nova `1a05dfd8ae3651c9`), confirmação registrada na
  thread original. `estado/newsletter/aprovacoes/2026-09-01/meta.json`
  atualizado para `status: "enviado_equipe"`.

- **2026-09-01 17:35 UTC — teste validado; parágrafo de abertura removido;
  envio real à equipe.** Usuário aprovou o teste e pediu duas coisas: (1)
  remover o parágrafo editorial de abertura ("1º de setembro de 2026...",
  logo abaixo do título) — não via propósito nele; (2) já que o teste
  funcionou, mandar a edição de hoje (sem esse parágrafo) para a equipe de
  verdade. Removido de `templates/email_newsletter.html` (bloco "PARÁGRAFO
  EDITORIAL DE ABERTURA") e de `SKILL.md`; edição de hoje segue direto do
  título para o "Resumo executivo". `newsletter.html` do dia corrigido e
  reenviado como mensagem nova (sem Fwd:) para
  escritafiscal.centralizada@copasul.coop.br às 17:35 UTC (thread
  `1a05e0450ef58655`). `destino_override` removido do `meta.json` — o teste
  encerrou; a partir de amanhã o ciclo roda com o destino real de produção.

- **2026-09-02 11:40 UTC — 6ª edição de produção, 2 itens.** Pré-voo:
  `MODO=COMPLETO` (3/8 fontes primárias alcançáveis: gov.br, cgibs.gov.br,
  cfc.org.br OK; planalto.gov.br, in.gov.br, portal.stf.jus.br,
  confaz.fazenda.gov.br bloqueados com http=000, stj.jus.br com HTTP 403;
  imprensa especializada toda acessível; push testado e funcional).
  Pesquisa conduzida diretamente nesta sessão (WebSearch/WebFetch, sem
  delegar ao agente `pesquisador-fiscal`), cerca de 16 buscas ao todo,
  acima do orçamento sugerido de 10 em `pesquisa.md` pela dificuldade de
  achar fato genuinamente dentro da janela de 24h; nenhuma norma de
  CONFAZ/STF/STJ entrou na edição (fontes bloqueadas), então não foi
  necessário aplicar a regra dos dois independentes. Dois itens com fonte
  primária verificada diretamente: (1) eixo tributário, Receita Federal
  disponibiliza em 01/09 o Perguntas e Respostas do ITR 2026, atualizado
  até 22/06, no fechamento do prazo da DITR (10/08 a 30/09, IN RFB
  2.330/2026); (2) eixo reforma, comunicado da Receita Federal de 01/09
  confirma a abertura, até 30/09, da janela de opção pelo modelo de
  recolhimento de IBS/CBS no Simples Nacional para 2027, tratado como
  atualização do que já foi coberto em 01/09 (Resolução CGSN 186/2026):
  o comunicado de hoje detalhou os modelos puro e híbrido regulamentados
  pelas Resoluções CGSN 190 e 191/2026 (11/08), desdobramento novo, não
  repetição. Dentro do mesmo item, entrou como contexto (não como item
  autônomo, por ter fato-data de 31/08, fora da janela estrita de 24h) a
  implantação em produção pela SVRS do conjunto de Notas Técnicas
  2026.002 para nove documentos fiscais eletrônicos. Eixo contabilidade:
  0 achados com consequência normativa nas últimas 24h (cfc.org.br
  acessível e checado diretamente; achados do dia foram só evento/curso e
  coordenação institucional sobre bloqueio de acesso ao "Meu Imposto de
  Renda", sem fato normativo). Descartados por ficarem fora da janela de
  24h mesmo sendo relevantes: adiamento do split payment obrigatório para
  2028 (matéria de 30/08) e Solução de Consulta Cosit 144/2026 sobre
  PIS/Cofins em depreciação de imóveis (matéria de 31/08). Edição com
  2.002 palavras visíveis (contagem por strip de tags), dentro da faixa de
  10-15 min. Enviada via `mcp__Gmail__send_message` para
  luis.santos@copasul.coop.br às 11:40:35 UTC, thread `1a061ebc12e560f0`,
  confirmada entregue via `get_thread` (29,8 KB). `newsletter.html` salvo
  em `estado/newsletter/aprovacoes/2026-09-02/` e `meta.json` criado com
  `status: "aguardando_decisao"`. Ferramenta `send_later` (MCP
  claude-code-remote) não estava registrada nesta sessão; o check-in de
  30 min para a etapa de distribuição (`newsletter-aprovacao`) foi
  agendado com `CronCreate` (job `c3f22ee8`, one-shot, 12:10 UTC) como
  substituto funcional. Ressalva: jobs de `CronCreate` são só de sessão
  (não persistem em disco); se esta sessão encerrar antes de 12:10 UTC, o
  check-in não dispara e a decisão de distribuição de hoje fica pendente
  até alguém invocar `newsletter-aprovacao` manualmente ou sob demanda.

- **2026-09-03 10:08-13:21 UTC — 7ª edição de produção, com falha
  operacional de dedup a registrar.** Erro no início da sessão: o checkout
  inicial (`git fetch` + `git checkout` do branch) não foi seguido de
  `git pull`, então a sessão trabalhou por toda a pesquisa e redação com uma
  cópia de `enviados.json` e `log.md` **22 commits desatualizada**, sem
  visibilidade das edições de produção de 08-29, 09-01 e 09-02 (nem do ciclo
  de distribuição à equipe criado nesse meio-tempo). Consequência concreta:
  o item "abertura do prazo de opção Simples Nacional 2027 e escolha entre
  Simples Puro e Simples Híbrido para IBS/CBS" foi redigido e enviado nesta
  edição como se fosse achado novo, usando inclusive a mesma URL de fonte
  (gov.br, "cgsn-atualiza-regras-do-simples-nacional...") já registrada em
  `enviados.json` desde 02/09 sob o título "Resoluções CGSN 190 e 191/2026
  detalham os modelos puro e híbrido de IBS/CBS no Simples Nacional para
  2027", e cujo fato-base (abertura da janela) já tinha sido coberto também
  em 01/09 via Resolução CGSN 186/2026. O conteúdo em si está correto
  (verificado em fonte primária, sem erro factual), mas violou a regra de
  não repetir achado já coberto nos últimos 7 dias sem desdobramento real:
  não havia desdobramento genuíno em relação ao que já saiu em 01 e 02/09,
  só um ângulo de redação diferente (o alerta de abertura do prazo em vez do
  detalhamento dos modelos). Detectado só depois do envio, ao tentar dar
  commit no estado e encontrar conflito de merge com o `enviados.json` e
  `log.md` reais. Correção aplicada: **não** foi adicionada entrada nova em
  `enviados.json` para esse item (ele já está coberto pelas entradas de
  01 e 02/09, mantidas); e este registro de log documenta o erro em vez de
  encobri-lo. Não houve reenvio de e-mail corretivo nesta sessão: o e-mail
  já está entregue e seu conteúdo não está factualmente errado, só
  redundante em um dos três itens; reenviar geraria uma segunda edição no
  mesmo dia, o que a invariante do dia proíbe.
  Pré-voo (rodado antes do problema acima ser percebido): MODO=COMPLETO
  (3/8 fontes primárias alcançáveis: gov.br, cgibs.gov.br, cfc.org.br; toda a
  imprensa listada acessível; bloqueados: planalto.gov.br, in.gov.br,
  portal.stf.jus.br, stj.jus.br, confaz.fazenda.gov.br). Push de teste do
  pré-voo (dry-run) acusou BLOQUEADO por estar atrás do remoto (mesma causa
  do problema de dedup); o push real desta edição, feito depois do
  `git pull --ff-only`, funcionou normalmente, sem `AVISO=SEM_PERSISTENCIA`
  a repassar ao usuário. Pesquisa via agente `pesquisador-fiscal` (17
  WebSearch, acima do orçamento de ~10, pela dificuldade de separar
  prazo/norma real de artigo de opinião) seguida de verificação manual em
  fonte primária de cada achado antes de escrever, como manda o protocolo.
  A verificação manual corrigiu um erro factual do dossiê do agente: ele
  descreveu a IN RFB 2.341/2026 como medida mais dura para devedor
  contumaz e Cadin; a leitura direta do texto em gov.br mostrou o oposto
  (prazo de regularização sobe de 20 para 30 dias úteis, devedor contumaz
  fica expressamente fora dessa regra, Confia/Sintonia ganham prazo
  extra). 3 itens na edição: (1) IN RFB 2.341/2026, genuinamente novo,
  verificação primária, fonte aberta diretamente em gov.br, adicionado a
  `enviados.json`; (2) Ajuste SINIEF 26/2026 (CT-e Simplificado, mesmo
  município para mesma UF), genuinamente novo, verificação
  dupla_secundaria (texto oficial do CONFAZ retornou HTTP 503 na janela de
  pesquisa, confirmado via Contábeis, aberto diretamente, e decreto de
  incorporação do RICMS/RS; incorporação pelo RICMS/MS não confirmada,
  registrado como ressalva no e-mail), adicionado a `enviados.json`; (3)
  abertura do prazo de opção Simples Nacional 2027 e escolha Simples
  Puro/Híbrido para IBS/CBS, verificação primária (duas notícias da
  Receita Federal abertas diretamente), mas repetição não intencional do
  que já saiu em 01 e 02/09 (ver acima), não adicionado a `enviados.json`
  por já estar coberto. Um detalhe de "split payment" mencionado pelo
  agente de pesquisa não foi confirmado nas fontes primárias abertas
  manualmente e entrou apenas como ressalva não confirmada no Radar, não
  como afirmação de fato. Contabilidade: 0 itens na janela de 24h, seção
  omitida (CFC, CPC e CVM sem novidade nas últimas 24-48h). Edição com
  1.944 palavras (~10 min de leitura), conferida sem travessão, sem
  `<img>` e sem `background` sem `-color` antes do envio. E-mail enviado
  para luis.santos@copasul.coop.br, thread 1a0676db46c3f4df, confirmado
  entregue em tamanho completo (27,9 KB, todos os links e cores
  preservados).
  Lição para a próxima execução: sempre `git pull --ff-only` logo após o
  checkout inicial, antes de ler qualquer arquivo de `estado/`, mesmo que
  a instrução do disparo diga só para fazer `checkout`.

- **2026-09-03 (mesma sessão) — usuário perguntou, ao vivo e fora do fluxo
  agendado, se a newsletter de 02/09 foi distribuída para a equipe.**
  Verificação na thread `1a061ebc12e560f0`: Luis respondeu "ENVIAR" às
  2026-09-02T11:46:33Z, mas `estado/newsletter/aprovacoes/2026-09-02/meta.json`
  permaneceu com `status: "aguardando_decisao"` porque o check-in de
  distribuição daquele dia foi agendado só via `CronCreate` (job de sessão,
  não persiste em disco) e a sessão que o criou aparentemente encerrou antes
  de disparar. Resultado: a aprovação existe, mas a distribuição para
  escritafiscal.centralizada@copasul.coop.br nunca aconteceu. Resposta dada
  ao usuário no chat; ação de correção (rodar `newsletter-aprovacao`
  manualmente para concluir o ciclo de 02/09) fica a critério do usuário,
  não executada automaticamente nesta sessão por não fazer parte do escopo
  do disparo agendado de hoje.
