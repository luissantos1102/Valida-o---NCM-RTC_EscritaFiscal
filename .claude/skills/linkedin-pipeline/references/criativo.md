# Criativo / carrossel

## Escolha do formato

| Situação | Formato |
|---|---|
| A pauta tem etapas, prazos, comparação antes/depois, ou 3+ pontos que se sustentam sozinhos | **Carrossel**, 5 a 8 slides |
| A pauta é uma tese única, uma decisão pontual, um número que fala sozinho | **Criativo único** (um slide de capa + um de fecho) |

Na dúvida, carrossel: ele segura o leitor por mais tempo e é o formato que melhor
performa para conteúdo técnico.

Especificação: **1080 x 1350 px** (4:5, retrato — ocupa mais tela no feed).

## Produção: `bin/carrossel.py`

Você **não escreve HTML**. Escreve o roteiro em
`estado/publicacoes/<pacote>/roteiro.json` e roda:

```
python3 bin/carrossel.py estado/publicacoes/<AAAA-MM-DD>-<slug>
```

Saem os PNGs em `<pacote>/criativo/slide-NN.png`, já em 1080x1350, com a
identidade visual fixa. Os HTML intermediários ficam em `criativo/html/` — úteis
para depurar um slide que estourou.

Modelo completo: `bin/roteiro.exemplo.json`. Em qualquer campo de texto,
`**assim**` vira destaque na cor de realce.

### Tipos de slide

| tipo | campos | quando usar |
|---|---|---|
| `capa` | kicker, titulo, fonte, destaque | slide 1, sempre |
| `texto` | kicker, titulo, corpo[] | desenvolvimento de uma ideia |
| `comparativo` | kicker, blocos[{lab,val}], rodape | duas rotas, antes × depois, dois regimes |
| `lista` | kicker, titulo, itens[] | passos, obrigações, fundamentos de uma tese |
| `dados` | kicker, itens[{n,d}], rodape | prazos, percentuais, valores — grade 2x2 |
| `fecho` | kicker, titulo, assinatura[] | último slide, sempre |

Quebra de linha dentro de `val` (comparativo): use `\n`.

## Roteiro: o que escrever

O carrossel não repete a legenda. Ele é o **esqueleto visual** do argumento.

O carrossel segue o eixo do texto: **é o argumento jurídico em slides**, não um
passo a passo operacional. Se os slides do meio viraram uma lista de tarefas de
sistema, o roteiro escorregou — refaça a partir da análise.

- **Capa.** A tese jurídica em no máximo 8 palavras. Sem "arrasta pro lado". O campo
  `fonte` leva a referência normativa; `destaque` leva a data (DOU, julgamento).
- **Miolo.** Uma ideia por slide. Máximo 25 palavras de corpo por slide. Se não
  couber, a ideia vira dois slides — nunca reduza a fonte para caber.
- **Fecho.** O que vigiar, e a assinatura
  `["Luis Santos", "Direito Tributário e Análise de Dados Fiscais"]`.

Nunca coloque no criativo um número de lei que não foi verificado. Erro em imagem
não se corrige depois de publicado.

## Identidade visual: o que é fixo, o que varia

Duas armadilhas opostas. Um feed onde todo post é idêntico faz o leitor parar de
ver — o olho reconhece e pula. Um feed sem constância faz o leitor não reconhecer
o autor. A saída é separar o que se repete do que muda.

**Fixo em toda publicação** (está travado em `bin/temas.py`, não mexa por post):
fundo marinho `#0B1B2E`, acento âmbar `#D6A544`, faixa âmbar na capa, assinatura
no fecho, numeração no rodapé, formato 1080x1350.

**Varia conforme o conteúdo**: o template, declarado no `roteiro.json`.

| Template | Quando | Como se apresenta |
|---|---|---|
| `editorial` | Análise doutrinária, tese que se desenvolve em prosa. É o padrão | Título em serifa Charter, régua curta, muito respiro |
| `dossie` | Prazos, percentuais, comparação de regimes, retrospecto de semana | Sans display, grade de números, blocos de comparação |
| `tese` | Uma tese única e forte, com pouco texto | Serifa em corpo muito grande, alto contraste |

```json
{ "template": "editorial", "slides": [ ... ] }
```

**Não repita o template da publicação anterior** quando o conteúdo permitir
outro. O campo `ultimo_template` em `estado/rodizio.json` registra qual foi o
último; consulte antes de escolher. Se o conteúdo pedir mesmo o mesmo template
duas vezes seguidas — dois posts de prazos, por exemplo — use, mas varie a
estrutura interna: onde antes veio `comparativo`, use `dados` ou `lista`.

O template serve ao conteúdo, nunca o contrário. Não force um `dossie` num tema
que não tem números, só para variar.

## Verificação final (obrigatória)

Abra ao menos **a capa e o slide mais denso** e confira:

- [ ] Texto legível em miniatura (reduza a 300px e leia o título).
- [ ] Nada cortado nem encostando na borda.
- [ ] Cada referência normativa conferida contra o dossiê.
- [ ] Ordem dos slides correta na numeração dos arquivos.

Se um slide estourou a altura, o corpo está longo demais: corte texto ou divida
em dois slides. Não reduza a fonte.

## Como o carrossel chega ao LinkedIn

Os PNGs saem direto daqui para `bin/publicar_linkedin.py`, como post
**multi-imagem** — não como Documento/PDF. Decisão do usuário: o post de
Documento tem visual de leitura de slide, e ele já verificou que o multi-imagem
engaja melhor. Isso também significa que **nada muda nesta etapa** por causa da
publicação — o formato de saída (PNG, 1080x1350) já era o que a etapa 6 precisa.

## Sobre o Canva

O conector Canva **não serve** para este passo, e isso já foi testado:

- `generate-design-structured` só produz `presentation` (16:9) e exige que o
  usuário aprove um outline num widget interativo;
- `generate-design` com `instagram_post` sai em 1080x1350, mas gera um
  *candidato* único que precisa de escolha humana via `create-design-from-candidate`.

Nenhum dos dois produz um carrossel de 5 a 8 slides sem intervenção — o que mata
a automação. Não tente de novo por conta própria.

O Canva continua útil **depois**: se o usuário quiser retrabalhar um slide à mão,
suba o PNG com `mcp__Canva__upload-asset-from-url` ou pelo próprio Canva.
