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
| `lista` | kicker, titulo, itens[] | passos, obrigações, o que fazer |
| `fecho` | kicker, titulo, assinatura[] | último slide, sempre |

Quebra de linha dentro de `val` (comparativo): use `\n`.

## Roteiro: o que escrever

O carrossel não repete a legenda. Ele é o **esqueleto visual** do argumento.

- **Capa.** A tese em no máximo 8 palavras. Sem "arrasta pro lado". O campo
  `fonte` leva a referência normativa; `destaque` leva a data (DOU, julgamento).
- **Miolo.** Uma ideia por slide. Máximo 25 palavras de corpo por slide. Se não
  couber, a ideia vira dois slides — nunca reduza a fonte para caber.
- **Fecho.** O que vigiar, e a assinatura
  `["Luis Santos", "Direito Tributário e Análise de Dados Fiscais"]`.

Nunca coloque no criativo um número de lei que não foi verificado. Erro em imagem
não se corrige depois de publicado.

## Identidade visual

Está travada no `bin/carrossel.py` e **não muda entre publicações** — é o que faz
a rede reconhecer o autor antes de ler o nome. Fundo petróleo `#0E2A25`, texto
`#F4F7F5`, realce verde `#6FCF9F` usado só no dado que importa. Sem foto de banco
de imagens. Se um dia precisar mexer na paleta, mexa no script, não no roteiro.

## Verificação final (obrigatória)

Abra ao menos **a capa e o slide mais denso** e confira:

- [ ] Texto legível em miniatura (reduza a 300px e leia o título).
- [ ] Nada cortado nem encostando na borda.
- [ ] Cada referência normativa conferida contra o dossiê.
- [ ] Ordem dos slides correta na numeração dos arquivos.

Se um slide estourou a altura, o corpo está longo demais: corte texto ou divida
em dois slides. Não reduza a fonte.

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
