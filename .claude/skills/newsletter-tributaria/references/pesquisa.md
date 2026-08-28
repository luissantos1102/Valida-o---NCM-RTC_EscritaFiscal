# Papel: pesquisador

Missão: mapear tudo que **efetivamente se moveu** nas últimas 24h nos três eixos
da newsletter, com fonte identificável. Ao contrário do pipeline do LinkedIn,
aqui não se filtra por potencial de post nem por ângulo Copasul — é digest, não
pauta editorial. Cobertura ampla é o objetivo.

## Antes de tudo: pré-voo de rede

```
bash bin/preflight.sh
```

- **MODO=COMPLETO** → siga este arquivo como está escrito.
- **MODO=DEGRADADO** → siga também a seção "Modo degradado", no fim.

## Janela

`agora - 24h` até `agora`. Nada anterior entra como item novo. Um fato de fora
da janela só aparece se for **desdobramento direto** de algo já coberto (ex.:
prazo que vence hoje de uma norma publicada semana passada) — e nesse caso
entra como atualização, não como item novo.

## Orçamento de busca

Até **10 chamadas de `WebSearch`** por execução (mais que o pipeline do
LinkedIn, porque aqui são três eixos e cobertura ampla, não uma pauta só).
Distribua por eixo — 3 a 4 buscas cada — e gaste `WebFetch` para abrir a fonte
primária de cada achado, não para "confirmar de novo" o que duas fontes já
bateram.

## Onde procurar, por eixo

**Direito Tributário (geral, além da Reforma)**
- Receita Federal: instruções normativas, soluções de consulta, notas técnicas,
  atos declaratórios.
- CONFAZ: convênios e ajustes SINIEF.
- STF e STJ: julgamentos, repercussão geral, temas repetitivos, modulação de
  efeitos. Use `mcp__Jusratio__pesquisar_documentos` e
  `mcp__Jusratio__informativo_juridico`, priorizando autoridade A e B.
- CARF: acórdãos e mudanças de entendimento.
- Estados/municípios: mudanças relevantes de ICMS/ISS que repercutam nacionalmente
  (via imprensa especializada, não é preciso varrer todos os 27 estados).

**Reforma Tributária (IBS/CBS)**
- Portal do Planalto / DOU: leis, MPs, decretos.
- Comitê Gestor do IBS e Secretaria Extraordinária da Reforma Tributária:
  regulamentações da LC 214/25 e da LC 227/2026, notas técnicas, cronogramas,
  layouts de NF-e/NFS-e com campos de IBS/CBS, split payment.
- Congresso Nacional: andamento de PLPs regulamentadores (marque como
  **projeto**, nunca como norma vigente).

**Contabilidade**
- CFC (Conselho Federal de Contabilidade): Normas Brasileiras de Contabilidade
  (NBCs), resoluções.
- CPC (Comitê de Pronunciamentos Contábeis): pronunciamentos novos ou revisados.
- CVM: instruções relevantes para contabilidade societária, quando repercutirem
  além de capital aberto.
- IASB/IFRS: mudanças de norma internacional com efeito de convergência no
  Brasil (menor prioridade — só entra se já houver repercussão nacional).

**Imprensa especializada (termômetro, nunca âncora sozinha)**
- Conjur, JOTA, Migalhas, Valor Econômico, Contábeis, Portal Contábeis.

## O que NÃO é fato normativo

Mesma régua do pipeline do LinkedIn: precisa ser um **ato com consequência
jurídica ou contábil** — norma publicada, decisão judicial/administrativa,
prazo que corre, consulta respondida, pronunciamento contábil editado. Curso,
webinar, release institucional sem norma anexa, artigo de opinião e agenda
divulgada não contam como item — podem aparecer como contexto de um item real.

## Saída desta etapa

Um dossiê com todos os achados das últimas 24h (pode ser 0, pode ser 15 — não
force um número). Para cada um:

```
- titulo:         frase curta do que aconteceu
  eixo:           tributario | reforma | contabilidade
  data:           AAAA-MM-DD (do fato, não da matéria)
  fonte_primaria: URL + identificação (ex.: "IN RFB 2.xxx/2026, art. 5º")
  tipo:           norma_vigente | projeto_proposta | decisao_judicial | pronunciamento_contabil
  por_que_importa: 1-2 frases, sem jargão desnecessário
```

Regras:
- Nunca cite norma sem ter aberto a fonte primária. Se o número não confere,
  descarte o achado.
- Marque explicitamente o que é **projeto/proposta** e o que é **norma vigente**.
- Cruze com `estado/newsletter/enviados.json` antes de finalizar o dossiê —
  itens já cobertos nos últimos 7 dias sem desdobramento novo saem da lista.

## Modo degradado

Quando o pré-voo acusa egresso bloqueado para fonte primária:

1. **Regra dos dois independentes.** Cada número de norma, artigo e data só
   entra se **duas fontes secundárias sem relação entre si** trouxerem o mesmo
   dado. Sem isso, o dado não entra, ou entra sem o número.
2. **Marque o nível.** Cada achado leva
   `verificacao: primaria | dupla_secundaria | unica_secundaria`. Nada com
   `unica_secundaria` vira afirmação na newsletter.
3. **Registre no `log.md` e no e-mail.** A newsletter abre avisando que saiu em
   modo degradado.

Diga ao usuário, uma vez por execução em modo degradado, que a correção é
liberar os domínios de `bin/preflight.sh` na política de rede do ambiente.
