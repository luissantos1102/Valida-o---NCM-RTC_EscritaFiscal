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
3. **Criativo** — os slides embutidos como imagem, na ordem, e anexados em PNG.
4. **Por que este tema** — a tabela de pontuação, o bloco FATO/TENSÃO/ÂNGULO/
   CONSEQUÊNCIA e os dois parágrafos de justificativa.
5. **Fontes** — lista com URL e identificação normativa.
6. **Agendamento previsto** — data e hora: 17:30 do dia seguinte ao disparo.
7. **Rodízio** — eixo desta publicação e como fica a cota do mês.

Anexe os PNGs. Não dependa só das imagens embutidas.

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
