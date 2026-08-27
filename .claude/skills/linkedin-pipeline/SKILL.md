---
name: linkedin-pipeline
description: Produz uma publicação completa para o LinkedIn de Luis Santos (pesquisa de pauta quente dos últimos 5 dias, análise de engajamento, redação em tom acadêmico-jornalístico, criativo/carrossel) e envia para aprovação por e-mail. Use quando a Routine "LinkedIn — Produção de Conteúdo" disparar, ou quando o usuário pedir para "produzir o post do LinkedIn", "rodar o pipeline de conteúdo" ou "buscar pauta para o LinkedIn".
---

# Pipeline de conteúdo para LinkedIn

Você opera três papéis em sequência — **pesquisador**, **analista de marketing** e
**roteirista/colunista** — para produzir UMA publicação por execução, e só encerra
quando o conteúdo estiver enviado para aprovação.

## Perfil do autor (nunca escreva fora dele)

Luis Santos. Setor fiscal e contábil da Copasul (cooperativa agrícola, Naviraí/MS),
Key User de Oracle EBS. Cursa Direito na UEMS. Faz a ponte entre operação fiscal e
sistemas: levanta requisitos, homologa melhorias, testa parametrizações. Constrói
dashboards (Power BI, Looker Studio) e automações (Python, VBA, GAS).

Frentes jurídicas: **Direito Tributário** (com ênfase em Reforma Tributária — IBS,
CBS, LC 214/25 e LC 227/2026), **Direito Empresarial** e **Direito Contratual**.

O diferencial que todo texto deve carregar implicitamente: ele entende a norma **e**
o sistema que precisa executá-la — enxerga o impacto de uma mudança legislativa
antes que ela vire custo ou passivo.

Objetivo das publicações: autoridade na rede, engajamento, network e oportunidades.

## Execução

Rode as 6 etapas na ordem. Não pule etapas nem antecipe a publicação — o LinkedIn
só é tocado **depois** da aprovação por e-mail, na skill `linkedin-aprovacao`.

### 1. Definir o tema da vez (rodízio)

Leia `estado/rodizio.json` na raiz do repositório e aplique
`references/rotacao.md` para descobrir qual eixo (Tributário / Empresarial /
Contratual) está em dívida no mês corrente. O eixo sugerido é uma **preferência**,
não uma trava: se a pesquisa da etapa 2 revelar um fato muito mais relevante em
outro eixo, você pode trocar — mas registre o motivo em `desvio_justificado` no
estado e compense no ciclo seguinte.

### 2. Pesquisar (papel: pesquisador)

Comece por `bash bin/preflight.sh`, que diz se este ambiente alcança as fontes
primárias. Depois siga `references/pesquisa.md` — inclusive a seção "Modo
degradado", se o pré-voo acusar bloqueio.

Regra dura: só entra na pauta o que teve movimento nos **últimos 5 dias**
contados da data de execução.

### 3. Analisar e decidir (papel: analista de marketing)

Siga `references/analise.md`. Você produz um ranking de 3 a 5 pautas candidatas,
pontuadas, e escolhe **uma**. Registre a pontuação — ela vira histórico.

### 4. Escrever (papel: roteirista/colunista)

Siga `references/redacao.md`. Tom acadêmico/jornalístico/informativo. Salve em
`<pacote>/texto.md` e rode `python3 bin/contar.py <pacote>/texto.md` **antes** da
checagem editorial — ele reprova tamanho, hashtags e fontes fora do protocolo.

### 5. Criar o visual

Siga `references/criativo.md`. Escreva o roteiro em `<pacote>/roteiro.json` e
rode `python3 bin/carrossel.py <pacote>`. Saem os PNGs em 1080x1350 com a
identidade fixa. Não escreva HTML à mão e não tente o Canva — o motivo está no
protocolo.

### 6. Enviar para aprovação

Siga `references/email.md`. Envie para **luis.santos@copasul.coop.br**, salve o
pacote em `estado/publicacoes/<AAAA-MM-DD>-<slug>/`, atualize
`estado/rodizio.json`, commite e faça push no branch de trabalho.

Depois de enviar, **agende o monitoramento da resposta**: chame `send_later`
(MCP claude-code-remote) com `delay_minutes: 30` e uma mensagem que instrua você
mesmo a invocar a skill `linkedin-aprovacao` para o pacote produzido. Encerre o
turno. Não fique em espera ativa, não use `sleep`.

## Invariantes

- Uma execução = uma publicação. Nunca produza duas.
- Se o pré-voo acusar `AVISO=SEM_PERSISTENCIA`, o container morre levando o estado
  junto. Não descubra isso no fim: **anexe `estado/rodizio.json` ao e-mail de
  aprovação** e diga ao usuário, em uma linha, que a cota do mês terá de ser
  reaplicada à mão e qual configuração corrige (o repositório em
  **Select repositories**, na edição da Routine).
- Nada vai ao LinkedIn sem o "aprovado" chegar por e-mail.
- Toda afirmação normativa carrega a fonte (número da lei/artigo, órgão, data),
  no nível de verificação que o ambiente permitiu — e em modo degradado o e-mail
  diz isso ao usuário, em vez de apresentar o pacote como verificado.
- Se a pesquisa não achar nada relevante nos 5 dias, **não invente pauta**: envie
  o e-mail explicando o vazio e propondo 3 temas perenes do eixo da vez, e peça
  a decisão. Isso conta como envio para aprovação.

## Ferramentas do repositório

| Script | Quando |
|---|---|
| `bin/preflight.sh` | início da etapa 2 — fontes primárias alcançáveis + o push funciona |
| `bin/contar.py` | fim da etapa 4 — reprova o texto fora dos limites do protocolo |
| `bin/carrossel.py` | etapa 5 — gera os PNGs a partir de `roteiro.json` |
| `bin/roteiro.exemplo.json` | modelo de roteiro, com os cinco tipos de slide |
