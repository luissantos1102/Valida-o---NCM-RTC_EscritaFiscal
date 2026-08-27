---
name: linkedin-aprovacao
description: Verifica a resposta de aprovação por e-mail de um pacote de conteúdo do LinkedIn e dá seguimento — publica e agenda no LinkedIn quando aprovado, ou abre a rodada de ajuste quando reprovado. Use quando um check-in agendado pedir para "verificar a aprovação do post do LinkedIn", quando chegar resposta na thread de aprovação, ou quando o usuário perguntar em que pé está um post enviado.
---

# Verificação de aprovação e seguimento

Esta skill é o segundo tempo do `linkedin-pipeline`. Ela é invocada por um
check-in agendado via `send_later`, ou sob demanda.

## 1. Localize o pacote

Se o check-in trouxer o caminho, use-o. Senão, pegue o pacote mais recente em
`estado/publicacoes/` cujo `meta.json` tenha `status` igual a
`aguardando_aprovacao`. Se não houver nenhum, não há o que fazer: encerre sem
agendar novo check-in.

Leia `meta.json`: `thread_id`, `rodada`, `assunto`, `eixo`, `data_agendamento`.

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
`status: "aguardando_direcionamento"`. Reagende check-in em 30 min.

**Escolha de caminho**:
- *ajustar o texto* → reescreva por `references/redacao.md` aplicando a crítica,
  refaça o criativo se necessário, reenvie como `(rev. N+1)`, incremente
  `rodada`, volte a `aguardando_aprovacao`, reagende check-in.
- *novo tema* → registre a pauta em `estado/rodizio.json` → `descartados`, e
  execute o `linkedin-pipeline` da etapa 2 em diante, produzindo pacote novo
  para a **mesma** data de agendamento (se ainda der tempo antes das 17:30; se
  não der, agende para o mesmo horário do dia seguinte e diga isso no e-mail).

**Sem resposta** → aplique a cadência de `references/email.md`: reagende em 30
min dentro da janela 7h–20h (UTC-4); fora dela, reagende para as 7h; lembrete
único ao meio-dia do dia do agendamento; expire em 48h com
`status: "expirado"`. Não escreva ao usuário nesta sessão a cada check-in
silencioso — apenas reagende.

**Ambíguo** → responda na thread pedindo a definição, em uma pergunta só, com as
opções nomeadas. Reagende check-in. Se continuar ambíguo na rodada seguinte,
assuma AJUSTAR O TEXTO e diga que assumiu.

## 5. Sempre

- Registre cada passagem em `log.md` do pacote (data/hora, classificação, ação).
- Commite e faça push a cada mudança de estado.
- Um check-in nunca termina sem uma destas três coisas: uma ação executada, um
  novo check-in agendado, ou o ciclo declarado encerrado (agendado ou expirado).
