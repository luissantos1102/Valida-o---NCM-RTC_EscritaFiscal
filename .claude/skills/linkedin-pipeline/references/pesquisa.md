# Papel: pesquisador

Missão: mapear o que **efetivamente se moveu** nos últimos 5 dias nos três eixos
de interesse, com fonte primária identificável.

## Antes de tudo: pré-voo de rede

```
bash bin/preflight.sh
```

Ele testa o egresso para as fontes primárias e diz o **MODO** da execução.
Rode sempre, no começo da pesquisa. O ambiente pode ter política de rede
restritiva, e descobrir isso no meio da redação custa a execução inteira.

- **MODO=COMPLETO** → siga este arquivo como está escrito.
- **MODO=DEGRADADO** → siga também a seção "Modo degradado", no fim.

## Janela

`hoje - 5 dias` até `hoje`. Nada anterior entra como pauta principal. Material
mais antigo só entra como **contexto** dentro de um post cuja âncora é recente.

## Orçamento de busca

**No máximo 6 chamadas de `WebSearch` por execução.** Cada resultado volta com
resumo longo, e oito buscas custam ~24 mil tokens — mais que todos os protocolos
somados. O limite não reduz a cobertura se você buscar com intenção:

- **Agrupe.** Uma busca por eixo cobre a semana inteira daquele eixo. Não gaste
  uma chamada por órgão.
- **Não confirme o que já sabe.** Se dois resultados já trouxeram a mesma norma
  com o mesmo número e data, isso é a dupla fonte independente — não busque uma
  terceira vez para "ter certeza".
- **Gaste `WebFetch`, não `WebSearch`.** Abrir a fonte primária é o que sustenta
  o texto e custa menos que uma busca. Buscar de novo sobre o mesmo achado é o
  gasto que não retorna nada.

Se as 6 buscas não produzirem achado suficiente, é sinal de janela vazia — siga a
regra de janela vazia do `SKILL.md`, não estenda o orçamento.

## Onde procurar

Cubra, no mínimo:

**Fonte primária (obrigatório — é o que sustenta o texto)**
- Portal do Planalto / DOU: leis, MPs, decretos publicados na janela.
- Receita Federal: instruções normativas, soluções de consulta, notas técnicas.
- CONFAZ: convênios e ajustes SINIEF.
- Comitê Gestor do IBS e Secretaria Extraordinária da Reforma Tributária:
  regulamentações da LC 214/25 e da LC 227/2026, notas técnicas, cronogramas,
  layouts (NF-e/NFS-e com campos de IBS/CBS).
- STF e STJ: julgamentos, repercussão geral, temas repetitivos, modulação.
  Use `mcp__Jusratio__pesquisar_documentos` e `mcp__Jusratio__informativo_juridico`
  quando o eixo for jurisprudencial — priorize autoridade A e B.
- CARF: acórdãos e mudanças de entendimento.

**Termômetro de repercussão (é o que informa a etapa de análise)**
- Imprensa especializada: Conjur, JOTA, Migalhas, Valor, Contábeis, Portal Contábeis.
- LinkedIn: busque `site:linkedin.com/posts <termo>` para ver o que a rede já
  está discutindo, quem publicou e com que ângulo.
- Blogs de escritórios e de software fiscal (movimento de mercado costuma
  antecipar dor operacional real).

## O que NÃO é fato normativo

A âncora da pauta tem que ser um **ato com consequência jurídica**: norma
publicada, decisão judicial ou administrativa, prazo que corre, consulta
respondida, regulamentação editada. Nada disso conta como âncora:

- curso, módulo de treinamento, seminário, webinar ou live — inclusive de órgão
  oficial. Que a Receita *ensine* um tema não muda o regime jurídico dele;
- release institucional sem norma anexa ("órgão X anuncia esforço para Y");
- artigo de escritório, post de LinkedIn, opinião de especialista;
- nota de entidade de classe, salvo quando reage a norma identificável;
- reunião realizada, agenda divulgada, projeto apenas protocolado.

Esses materiais servem como **contexto ou termômetro de repercussão** dentro de
um post ancorado numa norma real. Nunca como o fato que abre o texto.

O teste: *consigo apontar o dispositivo, a decisão ou o prazo que mudou?* Se a
resposta for "não, mas o assunto está em pauta", não é pauta — é assunto. Vá
para a norma que está por trás dele, ou pegue outro candidato.

## Eixos e o que conta como pauta

| Eixo | Conta como pauta |
|---|---|
| Direito Tributário | Reforma Tributária (IBS/CBS, LC 214/25, LC 227/2026), regulamentação infralegal, obrigações acessórias, split payment, crédito, transição, contencioso tributário, decisões do STF/STJ com efeito de caixa |
| Direito Empresarial | Societário, recuperação judicial e falência, governança, cooperativismo (Lei 5.764/71 e o ato cooperativo na reforma), responsabilidade de sócios e administradores, marco legal de garantias |
| Direito Contratual | Cláusulas fiscais em contratos (repasse de carga tributária pós-reforma), reequilíbrio econômico-financeiro, contratos de longo prazo na transição IBS/CBS, garantias, inadimplemento, contratos agro (barter, CPR) |

## Saída desta etapa

Um dossiê com 6 a 10 achados. Para cada um:

```
- titulo:        frase curta do que aconteceu
  eixo:          tributario | empresarial | contratual
  data:          AAAA-MM-DD (do fato, não da matéria)
  fonte_primaria: URL + identificação (ex.: "IN RFB 2.xxx/2026, art. 5º")
  repercussao:   quem já falou disso e onde (com URLs)
  angulo_copasul: em uma linha — o que isso muda na rotina fiscal/sistêmica de
                  quem opera Oracle EBS numa cooperativa agrícola. Escreva
                  "nenhum" se não houver; não force.
```

Regras:
- Nunca cite norma sem ter aberto a fonte primária. Se o número não confere,
  descarte o achado.
- Não confie em resumo de imprensa para afirmar o conteúdo de um artigo de lei.
- Marque explicitamente o que é **projeto/proposta** e o que é **norma vigente**.

## Modo degradado

Quando o pré-voo acusa egresso bloqueado para fonte primária, a regra "nenhuma
norma sem a fonte aberta" não pode ser cumprida. **Não trave a execução** — mas
também não finja que verificou. Opere assim:

1. **Regra dos dois independentes.** Cada número de norma, artigo e data só entra
   no texto se **duas fontes secundárias sem relação entre si** trouxerem o mesmo
   dado. Dois portais republicando o mesmo release contam como uma. Se só uma
   fonte afirma, o dado não entra — ou entra sem o número ("uma resolução
   publicada em agosto", não "a Resolução nº 190").
2. **Marque o nível.** No dossiê, cada achado leva
   `verificacao: primaria | dupla_secundaria | unica_secundaria`.
   Nada com `unica_secundaria` pode virar afirmação no post.
3. **Prefira o fato à minúcia.** Em modo degradado, escreva sobre o que a norma
   *faz*, que é robusto, e não sobre o inciso que a faz — que é frágil sem o texto
   à mão.
4. **Descarte o que depende de confirmação.** Resultado de julgamento, placar,
   trecho de voto: sem a fonte, não vira pauta. Escolha outro candidato.
5. **Registre no `log.md` e no e-mail.** O e-mail de aprovação abre com o aviso
   de que o pacote saiu em modo degradado e o que isso significa — o usuário
   precisa saber o que está aprovando.

Diga ao usuário, uma vez por execução, que a correção definitiva é liberar os
domínios listados em `bin/preflight.sh` na política de rede do ambiente.
