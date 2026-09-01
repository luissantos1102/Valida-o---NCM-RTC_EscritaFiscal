---
name: newsletter-aprovacao
description: Verifica se Luis Santos decidiu distribuir a newsletter tributária do dia para a equipe (escritafiscal.centralizada@copasul.coop.br) e dá seguimento — encaminha quando ele responder ENVIAR, ou encerra o ciclo sem distribuir. Use quando um check-in agendado pedir para "verificar a decisão de distribuição da newsletter", quando chegar resposta na thread da newsletter do dia, ou quando o usuário perguntar se a newsletter de hoje foi para a equipe.
---

# Verificação da decisão de distribuição

Segundo tempo do `newsletter-tributaria`. É invocada por um check-in agendado
via `send_later`, ou sob demanda. Só existe para a etapa de **distribuição
para a equipe** — o envio a Luis já aconteceu antes desta skill rodar.

## 1. Localize o ciclo do dia

Leia `estado/newsletter/aprovacoes/<AAAA-MM-DD>/meta.json` para a data que o
check-in trouxer. Sem data explícita, pegue a mais recente com `status` igual
a `aguardando_decisao`. Se não houver nenhum, não há o que fazer: encerre sem
agendar novo check-in.

Leia do `meta.json`: `thread_id`, `message_id`, `assunto`, `enviado_luis_em`.

## 2. Leia a thread

`mcp__Gmail__get_thread` com o `thread_id`. Considere apenas mensagens **de**
luis.santos@copasul.coop.br **posteriores** a `enviado_luis_em`. Ignore ecos
das suas próprias mensagens (respostas de confirmação, pedidos de definição).

## 3. Classifique a resposta

| Classificação | Sinais |
|---|---|
| **ENVIAR** | "enviar", "envia", "pode mandar", "manda para a equipe", "sim, envia" |
| **NÃO ENVIAR** | "não enviar", "não manda", "não", "negativo", "fica só comigo" |
| **Sem resposta** | nada novo na thread |
| **Ambíguo** | qualquer outra coisa |

A decisão precisa ser **inequívoca**. Na dúvida, trate como ambíguo. Silêncio
nunca é "ENVIAR".

## 4. Aja conforme a classificação

**ENVIAR** →
1. `mcp__Gmail__forward` com `messageId` = `message_id` do `meta.json`,
   `to: ["escritafiscal.centralizada@copasul.coop.br"]`. Sem `forwardText`
   (a edição já se explica sozinha) a menos que Luis tenha pedido algo
   específico na resposta.
2. `mcp__Gmail__reply` na mesma thread para Luis, confirmando: "Enviado para
   a equipe (escritafiscal.centralizada@copasul.coop.br) às HH:MM."
3. Atualize `meta.json`: `status: "enviado_equipe"`, acrescente
   `enviado_equipe_em`.
4. Fim do ciclo.

**NÃO ENVIAR** →
1. Atualize `meta.json`: `status: "nao_enviado"`, acrescente `decidido_em`.
2. Não responda a thread — Luis já sabe que decidiu não distribuir. Fim do
   ciclo.

**Sem resposta** →
- Dentro da janela 7h-19h (Campo Grande, UTC-4): reagende check-in em 30 min
  via `send_later`, instruindo a invocar esta skill para a mesma data. Não
  escreva ao usuário nesta sessão a cada check-in silencioso — apenas
  reagende.
- Fora da janela (antes das 7h ou às/depois das 19h): não reagende. Atualize
  `meta.json`: `status: "nao_enviado"`, `motivo: "sem_resposta_ate_19h"`. Fim
  do ciclo — a edição de amanhã começa um ciclo novo, independente deste.

**Ambíguo** →
- 1ª vez: `mcp__Gmail__reply` na thread perguntando a definição, em uma
  pergunta só: "Para eu seguir: ENVIAR para a equipe, ou Não enviar?".
  Reagende check-in em 30 min.
- Se continuar ambíguo na rodada seguinte (dentro da mesma janela do dia):
  trate como **NÃO ENVIAR** (default seguro — nunca distribua por presunção),
  registre `status: "nao_enviado"`, `motivo: "ambiguo_assumido_nao_enviar"`,
  e diga na thread que assumiu essa leitura.

## 5. Sempre

- Registre cada passagem em `estado/newsletter/log.md`: data/hora,
  classificação, ação tomada.
- Commite e faça push a cada mudança de estado.
- Um check-in nunca termina sem uma destas três coisas: uma ação executada
  (encaminhado ou marcado como não enviado), um novo check-in agendado, ou o
  ciclo já declarado encerrado em rodada anterior.
