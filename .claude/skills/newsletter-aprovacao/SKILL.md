---
name: newsletter-aprovacao
description: Verifica se Luis Santos decidiu distribuir a newsletter tributária do dia para a equipe (escritafiscal.centralizada@copasul.coop.br) e dá seguimento — encaminha quando ele responder ENVIAR, ou encerra o ciclo sem distribuir. Use quando um check-in agendado pedir para "verificar a decisão de distribuição da newsletter", quando chegar resposta na thread da newsletter do dia, ou quando o usuário perguntar se a newsletter de hoje foi para a equipe.
---

# Verificação da decisão de distribuição

Segundo tempo do `newsletter-tributaria`. É invocada pela Routine permanente
`trig_016J271dzoETCpJNUecUV22T` (cron horário, 7h-19h Campo Grande, seg-sex —
não por `send_later` autoagendado: essa abordagem foi tentada no pipeline do
LinkedIn e falhou duas vezes porque a ferramenta não estava disponível na
sessão que precisava chamá-la) ou sob demanda. Só existe para a etapa de
**distribuição para a equipe** — o envio a Luis já aconteceu antes desta
skill rodar.

## 1. Localize o ciclo do dia

Leia `estado/newsletter/aprovacoes/<AAAA-MM-DD>/meta.json` para a data que o
check-in trouxer. Sem data explícita, pegue a mais recente com `status` igual
a `aguardando_decisao`. Se não houver nenhum, não há o que fazer: encerre sem
alterar nada — a próxima checagem já está garantida pela Routine permanente,
não precisa ser agendada aqui.

Leia do `meta.json`: `thread_id`, `html_path`, `assunto`, `enviado_luis_em`, e
o opcional `destino_override`. Quando presente, use esse endereço no lugar de
`escritafiscal.centralizada@copasul.coop.br` — é um ciclo de teste (o
`meta.json` traz uma `nota` explicando). Sem esse campo, o destino é sempre a
equipe.

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
1. Leia o conteúdo de `html_path` (o HTML exato que foi enviado a Luis).
2. `mcp__Gmail__send_message` com `to: [<destino_override, se houver no
   meta.json; senão "escritafiscal.centralizada@copasul.coop.br">]`,
   `subject` = `assunto` do `meta.json` (sem prefixo "Fwd:" e sem citar a
   mensagem original) e `htmlBody` = esse conteúdo. É um envio novo, não um
   encaminhamento — o destinatário recebe a edição como e-mail próprio.
3. `mcp__Gmail__reply` na mesma thread para Luis, confirmando o envio e
   dizendo para qual endereço foi (o real, ou o de teste se houver
   `destino_override`).
4. Atualize `meta.json`: `status: "enviado_equipe"`, acrescente
   `enviado_equipe_em`.
5. Fim do ciclo.

**NÃO ENVIAR** →
1. Atualize `meta.json`: `status: "nao_enviado"`, acrescente `decidido_em`.
2. Não responda a thread — Luis já sabe que decidiu não distribuir. Fim do
   ciclo.

**Sem resposta** →
- Dentro da janela 7h-19h (Campo Grande, UTC-4): não faça nada além de
  confirmar no `log.md` que checou e não havia novidade. Não agende
  check-in — a Routine permanente cobre isso sozinha na próxima hora.
- Fora da janela (antes das 7h ou às/depois das 19h — só relevante se
  chamada sob demanda, já que a Routine permanente só dispara dentro dela):
  atualize `meta.json`: `status: "nao_enviado"`, `motivo:
  "sem_resposta_ate_19h"`. Fim do ciclo — a edição de amanhã começa um ciclo
  novo, independente deste.

**Ambíguo** →
- 1ª vez: `mcp__Gmail__reply` na thread perguntando a definição, em uma
  pergunta só: "Para eu seguir: ENVIAR para a equipe, ou Não enviar?". Não
  agende check-in.
- Se continuar ambíguo na checagem seguinte (dentro da mesma janela do dia):
  trate como **NÃO ENVIAR** (default seguro — nunca distribua por presunção),
  registre `status: "nao_enviado"`, `motivo: "ambiguo_assumido_nao_enviar"`,
  e diga na thread que assumiu essa leitura.

## 5. Sempre

- Registre cada passagem em `estado/newsletter/log.md`: data/hora,
  classificação, ação tomada.
- Commite e faça push a cada mudança de estado.
- Nunca chame `send_later` nem tente agendar seu próprio retorno — a Routine
  permanente já garante a próxima checagem. Um check-in termina quando a ação
  cabível foi executada (ou confirmado que não havia nada a fazer) e o estado
  ficou registrado.
