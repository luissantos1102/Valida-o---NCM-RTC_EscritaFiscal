# Envio e monitoramento da aprovação

Destinatário: **luis.santos@copasul.coop.br**
Ferramenta: conector Gmail (`mcp__Gmail__send_message`, `search_threads`,
`get_thread`, `reply`).

## Assunto

```
[LinkedIn] Aprovação — <tema em até 6 palavras> — <AAAA-MM-DD>
```

O assunto é a chave de rastreio. Não mude o assunto entre rodadas de revisão:
acrescente ` (rev. 2)`, ` (rev. 3)` ao final, preservando o resto — assim a
resposta cai na mesma thread.

## Corpo

Use `templates/email_aprovacao.html`. Ele traz, nesta ordem:

0. **Aviso de verificação** — só quando a execução rodou em modo degradado
   (ver `pesquisa.md`). Vai acima de tudo, dizendo quais fontes não puderam ser
   abertas e que os dados normativos foram confirmados por dupla fonte
   secundária. Sem isso o usuário aprova achando que está verificado.
1. **Como responder** — o bloco de instrução, sempre no topo.
2. **Texto da publicação** — exatamente como será colado, em bloco monoespaçado,
   com a contagem de caracteres.
3. **Criativo** — a folha de contato e o roteiro em texto. Ver "Como anexar o
   criativo", abaixo.
4. **Por que este tema** — a tabela de pontuação, o bloco FATO/TENSÃO/ÂNGULO/
   CONSEQUÊNCIA e os dois parágrafos de justificativa.
5. **Fontes** — lista com URL e identificação normativa.
6. **Agendamento previsto** — data e hora: 17:30 do dia seguinte ao disparo.
7. **Rodízio** — eixo desta publicação e como fica a cota do mês.

## Como anexar o criativo

A ferramenta de e-mail recebe anexo como **base64 dentro do próprio argumento**
(`attachments[].content`) — ela não aceita caminho de arquivo. Sete PNGs de
1080x1350 viram cerca de 800 KB de base64 numa única chamada: caro e sujeito a
truncamento. Por isso o anexo é **uma folha de contato**, não os sete slides.

```
python3 bin/folha_contato.py estado/publicacoes/<AAAA-MM-DD>-<slug>
```

Isso gera `criativo/folha-contato.png` e `folha-contato.png.b64`. O padrão são
1600 px de largura: cada slide sai com cerca de 390 px, legível no celular, e o
base64 fica em torno de 337 KB — cabe numa chamada.

**A resolução do e-mail não afeta a publicação.** O LinkedIn recebe os PNGs
1080x1350 originais, direto do pacote. A folha existe só para o usuário aprovar.
Medições que levaram a esse padrão, num carrossel de 7 slides:

| Opção | base64 | Cada slide |
|---|---|---|
| 7 PNGs em resolução cheia | 733 KB (~188k tokens) | 1080 px |
| Folha a 1600 px (**padrão**) | 337 KB | ~390 px |
| Folha a 900 px | 150 KB | ~225 px |

Anexar os sete em resolução cheia é possível, mas gasta ~188k tokens por
execução para exibir na tela do e-mail algo que será publicado a partir de outro
arquivo. Só faça isso se o usuário pedir explicitamente.

No `send_message`, monte **um** anexo:

```
attachments: [{
  filename: "carrossel-<slug>.png",
  mimeType: "image/png",
  content:  <conteúdo de folha-contato.png.b64>
}]
```

Se o `.b64` passar de 400 KB, o próprio script avisa: rode de novo com largura
menor (`... <pacote> 900`).

Junto da folha, escreva no corpo o **roteiro dos slides em texto** — kicker e
título de cada um, uma linha por slide. É o que permite aprovar por leitura, sem
depender da imagem renderizar no cliente de e-mail.

E aponte para a resolução cheia: os sete PNGs ficam commitados em
`estado/publicacoes/<pacote>/criativo/slide-01.png` … `slide-07.png`, no branch
`claude/linkedin-content-agent-7hnba3`. Cite o caminho no e-mail.

**Nunca** tente anexar os sete PNGs individuais, e **nunca** deixe o e-mail sair
sem criativo nenhum: sem ele o usuário não tem o que aprovar.

## Vocabulário de resposta (declare no e-mail)

| Resposta | Significado |
|---|---|
| `APROVADO` | Publicar e agendar para 17:30 do dia seguinte |
| `REFAZER` | Reprovado — abre a rodada de ajuste |
| `APROVADO COM AJUSTE: <instrução>` | Aplicar o ajuste e publicar sem novo aval |

Qualquer resposta é aceita em linguagem livre; interprete a intenção. Só trate
como aprovação quando ela for **inequívoca**. Silêncio nunca é aprovação.

## Monitoramento

Depois de enviar, agende o próprio retorno com `send_later`
(`delay_minutes: 30`), com uma mensagem que instrua a invocar a skill
`linkedin-aprovacao` para o pacote em
`estado/publicacoes/<AAAA-MM-DD>-<slug>/`. Encerre o turno — nada de espera ativa.

Cadência dos check-ins:
- a cada 30 min, das 7h às 20h (horário de Campo Grande, UTC-4);
- fora dessa janela, reagende para as 7h do dia seguinte;
- às 12h do dia do agendamento previsto, se ainda não houver resposta, envie
  **um** lembrete na mesma thread ("o agendamento das 17:30 de hoje depende
  deste aval") e continue os check-ins;
- passadas 48h sem resposta, pare os check-ins, registre `status: "expirado"`
  no pacote e não publique. O próximo ciclo segue normalmente.

## Fluxo de reprovação (`REFAZER`)

Responda **na mesma thread** (`mcp__Gmail__reply`) com exatamente duas opções:

```
Recebido. Para eu seguir, me diga qual caminho:

1) AJUSTAR O TEXTO — mantenho o tema e refaço a redação.
   Se puder, diga o que incomodou (ângulo, tom, tamanho, abertura, fecho).

2) NOVO TEMA — descarto esta pauta e volto à pesquisa, trazendo o
   segundo colocado da análise ou uma pauta nova.
```

- **AJUSTAR O TEXTO** → reescreva aplicando a crítica (`references/redacao.md`),
  refaça o criativo se o texto mudou de tese, e reenvie como `(rev. N)`.
- **NOVO TEMA** → volte à etapa 2 do pipeline, marque a pauta descartada em
  `estado/rodizio.json` → `descartados` (para não reaparecer) e produza um
  pacote novo.
- Se a resposta não escolher entre as duas, pergunte de novo, uma vez. Se ainda
  ficar ambíguo, assuma **AJUSTAR O TEXTO** e diga no e-mail que assumiu.

Repita o ciclo até vir uma aprovação inequívoca. Não há limite de rodadas, mas a
partir da 3ª, inclua no e-mail um resumo do que já foi tentado, para o usuário
ver o histórico sem abrir as mensagens anteriores.

## Registro

A cada envio, acrescente uma linha em
`estado/publicacoes/<AAAA-MM-DD>-<slug>/log.md`: data/hora, rodada, ação,
`thread_id` do Gmail. Commite e faça push a cada rodada.
