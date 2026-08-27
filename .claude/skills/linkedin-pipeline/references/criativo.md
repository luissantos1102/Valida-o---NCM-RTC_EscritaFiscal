# Criativo / carrossel

## Escolha do formato

| Situação | Formato |
|---|---|
| A pauta tem etapas, prazos, comparação antes/depois, ou 3+ pontos que se sustentam sozinhos | **Carrossel**, 5 a 8 slides |
| A pauta é uma tese única, uma decisão pontual, um número que fala sozinho | **Criativo único** |

Na dúvida, carrossel: ele segura o leitor por mais tempo e é o formato que
melhor performa para conteúdo técnico.

Especificação: **1080 x 1350 px** (4:5, retrato — ocupa mais tela no feed).

## Roteiro do carrossel

O carrossel não repete a legenda. Ele é o **esqueleto visual** do argumento.

- **Slide 1 — capa.** A tese em no máximo 8 palavras. Sem "arrasta pro lado".
  Subtítulo de uma linha com a referência normativa (ex.: "LC 214/2025, art. 12").
- **Slides 2 a N-1 — desenvolvimento.** Uma ideia por slide. Máximo 25 palavras
  por slide. Se precisar de mais, a ideia deve virar dois slides. Prefira
  estruturas visuais a parágrafos: linha do tempo, antes × depois, tabela de
  duas colunas, lista numerada de obrigações.
- **Slide N — fecho.** O que vigiar + assinatura discreta:
  "Luis Santos · Direito Tributário e Análise de Dados Fiscais".

Nunca coloque no criativo um número de lei que não foi verificado na fonte
primária. Erro em imagem não se corrige depois de publicado.

## Identidade visual (mantenha constante entre publicações)

- Paleta sóbria: fundo escuro (grafite/azul-petróleo), texto branco, **um** tom
  de destaque (verde ou âmbar) usado só para o dado que importa no slide.
- Tipografia sem serifa, peso alto no título, corpo em peso regular. Nada de
  fonte decorativa.
- Muito respiro. Se o slide parece cheio, corte texto — não reduza a fonte.
- Sem banco de imagens genérico (aperto de mãos, martelo de juiz, prédio de
  vidro). Se precisar de imagem, use gráfico, tabela ou diagrama do próprio dado.
- Contraste mínimo 4.5:1. O feed é lido no celular, no claro.

Constância visual é o que faz a rede reconhecer o autor antes de ler o nome.

## Produção — Canva (caminho primário)

1. `mcp__Canva__list-brand-kits` — se houver brand kit, use-o e mantenha-o em
   todas as publicações.
2. `mcp__Canva__search-designs` com o termo `linkedin-luis` — reaproveite o
   design da publicação anterior como base (`copy-design`) para manter a
   identidade. Só gere do zero na primeira execução.
3. Sem base anterior: `mcp__Canva__generate-design-structured` com o roteiro
   dos slides e a especificação visual acima.
4. Revise com `mcp__Canva__read-design` — confira **cada** número de lei, data e
   artigo contra o dossiê. Corrija com `mcp__Canva__edit-design`.
5. `mcp__Canva__export-design` em PNG. Salve os arquivos em
   `estado/publicacoes/<AAAA-MM-DD>-<slug>/criativo/` como `slide-01.png`, etc.
6. Nomeie o design no Canva como `linkedin-luis <AAAA-MM-DD> <slug>`.

Se o Canva falhar ou não estiver conectado: gere os slides com HTML + CSS
(mesma paleta e grid), renderize com Chromium headless em 1080x1350 e siga em
frente. Registre no e-mail que o criativo veio pelo caminho alternativo.

## Verificação final

- [ ] Todo texto legível em miniatura (teste: reduza a 300px e leia o título).
- [ ] Nenhum texto cortado ou encostando na borda (margem mínima 80px).
- [ ] Referências normativas conferidas uma a uma.
- [ ] Ordem dos slides correta nos nomes dos arquivos.
