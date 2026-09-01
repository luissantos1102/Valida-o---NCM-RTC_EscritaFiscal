# Análise — 2026-08-31

## Eixo sugerido pelo rodízio

`estado/rodizio.json` está com as cotas zeradas e `mes_referencia` em 2026-08,
mas há duas publicações de 27/08 em `estado/publicacoes/`, ambas do eixo
tributário (uma publicada, uma ainda aguardando aprovação). Reconciliando o
estado pelo diretório: tributário 1 publicado, empresarial 0, contratual 0.

Dívida: tributário 3, empresarial 2, contratual 2. Pela regra 3 de
`rotacao.md`, o eixo de maior dívida seria o tributário. Mas a seção
"Distribuição dentro do mês" manda evitar dois posts do mesmo eixo em sequência
havendo eixo com dívida pendente, e os dois últimos foram tributários. Eixo
sugerido desta execução, portanto: **Empresarial** (empata com contratual em 2 e
vence pela ordem de prioridade).

## Pontuação

Pesos: Recência 3, Impacto 3, Densidade 2, Autoridade jurídica 3, Vida útil 1,
Rodízio 2. Máximo 70.

| Candidato | Rec. (3) | Imp. (3) | Dens. (2) | Autor. (3) | Vida (1) | Rod. (2) | Total |
|---|---|---|---|---|---|---|---|
| IN RFB 2.339/2026 — redutores do Sintonia | 5 = 15 | 4 = 12 | 3 = 6 | 5 = 15 | 4 = 4 | 2 = 4 | **56** |
| Malha Fiscal Digital PIS/Cofins | 5 = 15 | 4 = 12 | 2 = 4 | 3 = 9 | 3 = 3 | 2 = 4 | 47 |
| STF — voto de qualidade no CARF | descartado: sem fonte primária (filtro b) | | | | | | — |
| STJ — Emenda Regimental 48/2026 | descartado: sem fonte primária e sem data (filtro b) | | | | | | — |
| Empresarial / Contratual | sem candidato na janela | | | | | | 0 |

Escolhida: **IN RFB nº 2.339/2026**, 56 pontos.

## Desvio do rodízio

O eixo sugerido era o empresarial e o escolhido é o tributário. O desvio é
legítimo pela regra de `rotacao.md`: o melhor candidato do eixo sugerido não
existe (nenhum fato normativo empresarial ou contratual na janela de 5 dias,
depois de duas buscas dedicadas e da varredura do DOU e da imprensa), enquanto o
escolhido soma 56. A diferença supera com folga os 10 pontos exigidos.

Compensação: o eixo **empresarial** sobe ao topo de `fila_prioritaria` e fica
imune a novo desvio até ser publicado.

## Saturação

Sem busca dedicada no LinkedIn (orçamento de 6 `WebSearch` esgotado na pesquisa).
A leitura de saturação foi feita pela imprensa: até 31/08, nem Conjur, nem
Migalhas, nem JOTA haviam tratado da IN 2.339/2026, e o único material disponível
é o release da própria Receita, que descreve as mudanças como aperfeiçoamento
sem tocar no ponto jurídico. Tema não saturado, e o ângulo abaixo não está sendo
dito por ninguém.

## Ângulo

```
FATO:         A IN RFB nº 2.339, de 21/08/2026 (DOU de 28/08/2026, Seção 1,
              p. 62), alterou a IN RFB nº 2.316/2026 e criou dois redutores de
              nota no Programa Sintonia: 0,05 para procedimento fiscal encerrado
              com constituição de crédito tributário e 0,2 para representação
              penal formalizada.

TENSÃO:       Nenhum dos dois eventos é definitivo. O crédito constituído
              comporta impugnação; a representação penal é encaminhamento ao
              Ministério Público, não denúncia recebida nem condenação. A própria
              IN reconhece a provisoriedade (item 4.1.6.1 e art. 14, § 4º), mas
              não suspende o efeito enquanto a definitividade não vem.

ÂNGULO:       O Sintonia deixou de ser só um programa de prêmio e passou a operar
              como graduação com efeito antecipado: rebaixa primeiro e reabilita
              depois, de modo que o tempo do contencioso corre contra o
              classificado. E a IN pesa o indício quatro vezes mais que o crédito
              efetivamente constituído, assimetria que está no Anexo Único, não
              na lei instituidora.

CONSEQUÊNCIA: Quem depende do selo precisa tratar o prazo de impugnação e o
              pedido de revisão da classificação (art. 17) como um único
              problema, e vigiar o art. 9º, § 4º, que passou a admitir
              reclassificação fora do ciclo ordinário nos dois sentidos.
```

## Justificativa

A pauta se sustenta porque a questão jurídica está inteira dentro do texto que
foi aberto na fonte primária, sem depender de nenhuma norma que este ambiente
não alcançou. A tensão não é de implementação: é sobre o momento em que um ato
administrativo ainda sujeito a revisão pode produzir efeito desfavorável ao
contribuinte. E a demonstração é interna à própria instrução, que manda
desconsiderar o redutor em caso de nulidade ou total improcedência e restabelecer
o benefício se a conduta não for confirmada. Quem escreveu a norma sabia que o
pressuposto podia cair; só não tratou do intervalo entre o efeito e a decisão. É
aí que existe posição a sustentar, e é o tipo de leitura que constrói autoridade,
porque nasce da leitura do ato e não do noticiário sobre ele.

A segunda colocada, a Malha Fiscal Digital de PIS/Cofins, tem impacto de caixa
maior e prazo correndo até 30/10/2026, mas a discussão jurídica que ela abre
(alcance da espontaneidade depois do aviso de autorregularização) depende de
dispositivos do CTN e do Decreto nº 70.235/1972 que não puderam ser abertos,
porque planalto.gov.br está bloqueado neste ambiente. Escrever sobre ela exigiria
ou citar norma sem fonte, o que o protocolo proíbe, ou esvaziar o argumento até
sobrar descrição de procedimento. Fica registrada como candidata natural do
próximo ciclo tributário, se o acesso for liberado.
