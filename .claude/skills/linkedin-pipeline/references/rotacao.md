# Rodízio de temas

Meta: **8 publicações por mês**, distribuídas em

| Eixo | Publicações/mês |
|---|---|
| Direito Tributário | 4 |
| Direito Empresarial | 2 |
| Direito Contratual | 2 |

## Como decidir o eixo da execução

1. Leia `estado/rodizio.json`. Se `mes_referencia` for diferente do mês corrente
   (formato `AAAA-MM`), **vire o mês**: arquive `cotas` em `historico_mensal`,
   zere os contadores e atualize `mes_referencia`.
2. Calcule a **dívida** de cada eixo: `meta - publicado`.
3. O eixo sugerido é o de maior dívida. Empate → ordem de prioridade:
   Tributário → Empresarial → Contratual.
4. Passe o eixo sugerido para a etapa de pesquisa. A pesquisa varre os três
   eixos de qualquer forma; o eixo sugerido entra como peso na pontuação
   (critério "Aderência ao rodízio" em `analise.md`).

## Quando é legítimo furar o rodízio

Quando a pesquisa do dia trouxer, em outro eixo, um fato que pontue **10 pontos
ou mais acima** do melhor candidato do eixo sugerido. Nesse caso:

- publique o tema mais forte;
- grave `desvio_justificado` no registro da publicação, com a diferença de pontos;
- o eixo preterido sobe para o topo da fila no ciclo seguinte, ficando imune a
  novo desvio até ser publicado.

Isso mantém a proporção 4/2/2 fechando no mês sem engessar a relevância.

## Distribuição dentro do mês

Com disparo em segunda e quarta, o mês tem 8 ou 9 ciclos. Se houver um 9º ciclo,
ele vai para Tributário (o eixo de maior volume) e a meta do mês passa a 5/2/2.
Registre isso em `observacao` no estado.

Evite dois posts do mesmo eixo em sequência quando houver eixo com dívida
pendente — a alternância é o que faz o perfil parecer amplo em vez de monotemático.
