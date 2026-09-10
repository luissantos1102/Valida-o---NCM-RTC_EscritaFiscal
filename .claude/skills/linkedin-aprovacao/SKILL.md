---
name: linkedin-aprovacao
description: Verifica a resposta de aprovação por e-mail de um pacote de conteúdo do LinkedIn e dá seguimento — publica e agenda no LinkedIn quando aprovado, ou abre a rodada de ajuste quando reprovado. Use quando um check-in agendado pedir para "verificar a aprovação do post do LinkedIn", quando chegar resposta na thread de aprovação, ou quando o usuário perguntar em que pé está um post enviado.
---

# Verificação de aprovação e seguimento

Esta skill é o segundo tempo do `linkedin-pipeline`. Ela é invocada pela
Routine permanente `trig_01SAj9yvf6F4fk8MhPrpsYwD` (cron horário, 7h-19h
Campo Grande, seg-sex — não por `send_later` autoagendado: essa abordagem
falhou duas vezes, 02/09 e 09/09, porque a ferramenta não estava disponível
na sessão que precisava chamá-la) ou sob demanda.

## 1. Localize o pacote

Se o check-in trouxer o caminho, use-o. Senão, pegue o pacote mais recente em
`estado/publicacoes/` cujo `meta.json` tenha `status` igual a
`aguardando_aprovacao`, `aguardando_direcionamento` ou
`aguardando_decisao_tema`. Se não houver nenhum, não há o que fazer: encerre
sem alterar nada — a próxima checagem já está garantida pela Routine
permanente, não precisa ser agendada aqui.

Leia `meta.json`: `thread_id`, `rodada`, `assunto`, `eixo`, `data_agendamento`,
e (quando `status` for `aguardando_decisao_tema`) `temas_perenes_propostos`.

## 2. Leia a thread

`mcp__Gmail__get_thread` com o `thread_id`. Se não tiver o id, use
`mcp__Gmail__search_threads` pelo assunto.

Considere apenas mensagens **de** luis.santos@copasul.coop.br **posteriores** ao
último envio registrado em `log.md`. Ignore ecos das suas próprias mensagens.

## 3. Classifique a resposta

| Classificação | Sinais |
|---|---|
| **Aprovado** | "aprovado", "pode publicar", "ok, sobe", "positivo", "manda ver" |
| **Aprovado com ajuste** | aprovação + instrução pontual ("aprovado, só troca a abertura") |
| **Reprovado** | "refazer", "não", "negativo", "não gostei", "reprova" |
| **Escolha de caminho** | "ajustar o texto" / "novo tema" (resposta ao e-mail de reprovação) |
| **Sem resposta** | nada novo na thread |
| **Ambíguo** | qualquer outra coisa |

Aprovação precisa ser **inequívoca**. Na dúvida, trate como ambíguo. Silêncio
nunca é aprovação.

## 4. Aja conforme a classificação

**Aprovado** → siga `linkedin-pipeline/references/publicacao.md` inteiro.
Publique com agendamento para 17:30 do dia seguinte ao disparo, confirme por
e-mail com screenshot, atualize o estado, commite e push. Fim do ciclo.

**Aprovado com ajuste** → aplique o ajuste no texto (e no criativo, se o ajuste
mudar a tese), não peça novo aval, e siga para `publicacao.md`. Diga no e-mail
de confirmação exatamente o que foi alterado.

**Reprovado** → responda na mesma thread com as duas opções de
`references/email.md` (AJUSTAR O TEXTO / NOVO TEMA). Atualize `meta.json` para
`status: "aguardando_direcionamento"`. Não agende check-in — a Routine
permanente já vai passar de novo por este pacote na próxima hora.

**Escolha de caminho**:
- *ajustar o texto* → reescreva por `references/redacao.md` aplicando a crítica,
  refaça o criativo se necessário, reenvie como `(rev. N+1)`, incremente
  `rodada`, volte a `aguardando_aprovacao`.
- *novo tema* → registre a pauta em `estado/rodizio.json` → `descartados`, e
  execute o `linkedin-pipeline` da etapa 2 em diante, produzindo pacote novo
  para a **mesma** data de agendamento (se ainda der tempo antes das 17:30; se
  não der, agende para o mesmo horário do dia seguinte e diga isso no e-mail).

**Escolha de tema** (só quando `status` era `aguardando_decisao_tema` —
resposta ao e-mail de "janela vazia" propondo temas perenes): identifique qual
dos `temas_perenes_propostos` Luis escolheu (número ou descrição), ou um
ângulo novo que ele tenha proposto na resposta. Execute
`linkedin-pipeline` a partir da etapa 4 (redação) com esse tema — sem repetir
pesquisa/análise, já que o tema veio decidido —, gere o criativo, monte e
envie o e-mail de aprovação normal (`references/email.md`), sinalizando com
destaque se alguma fonte primária não pôde ser confirmada nesta execução.
Atualize `meta.json` para `status: "aguardando_aprovacao"` e registre `tema`,
`thread_id`/`message_id` do novo e-mail. Se a resposta trouxer, junto da
escolha, um pedido fora do escopo desta classificação (ex.: predefinir tema
para outra data), não tente executá-lo aqui: registre em `log.md` e responda
por e-mail perguntando separadamente.

**Sem resposta** → não faça nada além de confirmar no `log.md` que checou e
não havia novidade. Não agende check-in — a Routine permanente cobre isso
sozinha a cada hora (7h-19h Campo Grande, seg-sex). Às 12h do dia do
agendamento previsto, se ainda não houver resposta, envie **um** lembrete na
mesma thread ("o agendamento das 17:30 de hoje depende deste aval"). Passadas
48h sem resposta, marque `status: "expirado"` no pacote e não publique.

**Ambíguo** → responda na thread pedindo a definição, em uma pergunta só, com as
opções nomeadas. Não agende check-in. Se continuar ambíguo na checagem
seguinte, assuma AJUSTAR O TEXTO (ou, se o pacote estava em
`aguardando_decisao_tema`, o tema perene mais bem pontuado dos propostos) e
diga que assumiu.

## 5. Sempre

- Registre cada passagem em `log.md` do pacote (data/hora, classificação, ação).
- Commite e faça push a cada mudança de estado.
- Nunca chame `send_later` nem tente agendar seu próprio retorno — a Routine
  permanente já garante a próxima checagem. Um check-in termina quando a ação
  cabível foi executada (ou confirmado que não havia nada a fazer) e o estado
  ficou registrado; não há mais "reagendar" como responsabilidade desta skill.
