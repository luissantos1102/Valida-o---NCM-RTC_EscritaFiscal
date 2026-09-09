# Dossiê de pesquisa — janela 2026-09-04 a 2026-09-09

Executado em 2026-09-09. MODO=COMPLETO no pré-voo agregado (`www.gov.br`,
`www.cgibs.gov.br`, `cfc.org.br` acessíveis), mas com bloqueios pontuais
confirmados na prática para os dois candidatos mais fortes desta rodada
(`planalto.gov.br` e `bcb.gov.br`), testados diretamente por WebFetch além do
`curl` do preflight.

## Achados

### 1. LC 236/2026 — teto de multas e transação/mediação/arbitragem tributária
- Eixo: tributário · Data do fato: 2026-09-04
- Fonte primária: planalto.gov.br — **bloqueada** (503/captcha, confirmado por
  WebFetch direto em `ccivil_03/leis/lcp/lcp236.htm`).
- Verificação: dupla_secundaria (Migalhas + Senado Notícias, convergentes no
  número, data de sanção e teor: multa geral até 75% do tributo, 100% em
  fraude, 150% em reincidência).
- Não utilizável como âncora desta publicação: fonte primária não aberta.

### 2. Prazo de opção Simples Nacional / regime IBS-CBS 2027
- Eixo: tributário · Data: prazo corre até 30/09/2026
- Fonte primária: aberta e conferida (receita.fazenda.gov.br, Resoluções CGSN
  190/2026 e 191/2026).
- Descartado pelo filtro dos 60 dias (`estado/rodizio.json`): mesmo tema de
  "Simples Nacional no IBS/CBS", publicado em 27/08/2026. Reavaliar após
  27/10/2026.

### 3. RFB — consulta pública sobre regimes aduaneiros especiais de depósito
- Eixo: tributário · Data: 2026-09-04 (contribuições até 23/09/2026)
- Fonte primária: aberta e conferida (gov.br/receitafederal).
- Sem consequência jurídica firmada (é processo de consulta, não norma
  fechada) e sem ângulo Copasul (a cooperativa não opera entreposto/depósito
  aduaneiro especial). Autoridade jurídica e impacto prático baixos.

### 4. Resolução CMN nº 5.340/2026 — revisão de garantias em crédito rural
- Eixo: empresarial (marco legal de garantias, conforme tabela de
  `pesquisa.md`) · Data: 2026-09-04
- Fonte primária: bcb.gov.br — **bloqueada** (testado diretamente por WebFetch
  em duas URLs de normativo/PDF do BCB: uma devolveu apenas o cabeçalho da
  página, sem conteúdo; outra, 404).
- Verificação: dupla_secundaria (Poder360/Poder Agro + Portal do
  Cooperativismo Financeiro, convergentes no número, data e teor: revisão de
  garantias de crédito rural renegociado, prazo de contratação até
  12/11/2026, complementa a MP 1.376/2026).
- **Único achado empresarial dentro da janela de 5 dias.** Não utilizável
  como âncora: fonte primária não aberta, o que viola a regra que não se
  quebra desta execução ("nenhuma norma citada sem a fonte primária aberta e
  conferida").

### 5. Provimento CNJ nº 216/2026, art. 15, IV — ato cooperativo fora da
   recuperação judicial (OCB)
- Eixo: empresarial · Data do fato: ~2026-08-20 — **fora da janela de 5 dias**
- Já registrado e descartado em ciclos anteriores por essa mesma razão.
  Pesquisa desta rodada não encontrou nenhum desdobramento novo dentro de
  04–09/09/2026. `atos.cnj.jus.br` bloqueado (403); confirmação apenas por
  fontes secundárias de nicho (Sistema OCB), sem cobertura de imprensa
  jurídica geral.

## Conclusão da etapa de pesquisa

O eixo Empresarial — no topo da `fila_prioritaria`, imune a novo desvio desde
31/08/2026 — **não tem, nesta janela, nenhum fato normativo que atenda
simultaneamente aos dois requisitos duros**: (a) movimento nos últimos 5 dias
e (b) fonte primária aberta e conferida. O achado 4 cumpre (a) mas falha em
(b); o achado 5 cumpriria (b) se fosse aberto, mas falha em (a).

Isso caracteriza janela vazia para o eixo da vez, nos termos do `SKILL.md`.
