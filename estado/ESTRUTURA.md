# Estrutura do estado

O estado vive no repositório porque a sessão que executa o pipeline é efêmera —
o que não for commitado se perde quando o container é reciclado. **Cada mudança
de estado é seguida de commit e push.**

## `rodizio.json`

Controla a cota 4/2/2 do mês e a memória de temas.

| Campo | Uso |
|---|---|
| `mes_referencia` | `AAAA-MM`. Diferente do mês corrente → vira o mês (arquiva em `historico_mensal`, zera `cotas`) |
| `meta` | Cota mensal por eixo. Vira 5/2/2 num mês com 9 ciclos |
| `cotas` | Publicações já **agendadas** no mês, por eixo |
| `fila_prioritaria` | Eixos preteridos por desvio; entram na frente e ficam imunes a novo desvio |
| `historico` | `{data, eixo, tema, slug, url_post}` — usado para não repetir tema em 60 dias |
| `historico_mensal` | Fechamento de cada mês, para conferir a proporção ao longo do tempo |
| `descartados` | Pautas recusadas com "novo tema"; não voltam à análise |

## `publicacoes/<AAAA-MM-DD>-<slug>/`

Um diretório por ciclo de produção.

```
meta.json          estado do pacote (abaixo)
texto.md           texto final da publicação, pronto para colar
dossie.md          achados da pesquisa, com fontes
analise.md         tabela de pontuação + FATO/TENSÃO/ÂNGULO/CONSEQUÊNCIA
criativo/          slide-01.png … slide-0N.png
comprovante/       screenshots do agendamento no LinkedIn
log.md             uma linha por evento: data/hora, rodada, ação, thread_id
```

### `meta.json`

```json
{
  "slug": "split-payment-cronograma",
  "tema": "Split payment: o cronograma que o sistema ainda não executa",
  "eixo": "tributario",
  "data_producao": "2026-09-01",
  "data_agendamento": "2026-09-02T17:30:00-04:00",
  "status": "aguardando_aprovacao",
  "rodada": 1,
  "assunto_email": "[LinkedIn] Aprovação — Split payment cronograma — 2026-09-01",
  "thread_id": "",
  "desvio_justificado": null,
  "link_primeiro_comentario": null
}
```

`status` percorre:
`aguardando_aprovacao` → `aguardando_direcionamento` (se reprovado) →
`aguardando_aprovacao` (rev. N) → `agendado` | `expirado`.

## `newsletter/aprovacoes/<AAAA-MM-DD>/meta.json`

Um por edição da newsletter tributária, controla só a decisão de
**distribuição para a equipe** (o envio a Luis já saiu antes, sem aprovação).
Ver `.claude/skills/newsletter-aprovacao/SKILL.md`.

```json
{
  "data": "2026-09-01",
  "thread_id": "1a05d56163c38164",
  "html_path": "estado/newsletter/aprovacoes/2026-09-01/newsletter.html",
  "assunto": "Newsletter Tributária — 2026-09-01",
  "enviado_luis_em": "2026-09-01T14:21:32Z",
  "status": "aguardando_decisao"
}
```

A distribuição usa `html_path` com `mcp__Gmail__send_message` (envio novo,
mesmo assunto, sem "Fwd:") — nunca `mcp__Gmail__forward`, que prefixaria o
assunto e citaria a mensagem original abaixo.

`status` percorre:
`aguardando_decisao` → `enviado_equipe` | `nao_enviado`.
