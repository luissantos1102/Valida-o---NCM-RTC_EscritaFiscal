# Agente de conteúdo para LinkedIn

Pipeline automatizado que pesquisa pauta, decide tema, escreve o post, produz o
criativo, manda para aprovação por e-mail e — só depois do aval — publica e
agenda no LinkedIn.

Autor: Luis Santos — Direito Tributário, Empresarial e Contratual · Análise de
dados fiscais · Key User Oracle EBS.

## Como funciona

```
 seg/qua 07:00 (UTC-4)
        │
        ▼
 ┌──────────────────┐
 │ 1. RODÍZIO       │  qual eixo está em dívida no mês (4/2/2)
 ├──────────────────┤
 │ 2. PESQUISA      │  o que se moveu nos últimos 5 dias, com fonte primária
 ├──────────────────┤
 │ 3. ANÁLISE       │  pontua 3–5 pautas, mede saturação, escolhe uma
 ├──────────────────┤
 │ 4. REDAÇÃO       │  texto 1.300–1.900 car., tom acadêmico/jornalístico
 ├──────────────────┤
 │ 5. CRIATIVO      │  carrossel 5–8 slides ou imagem única, 1080x1350
 ├──────────────────┤
 │ 6. E-MAIL        │  → luis.santos@copasul.coop.br
 └────────┬─────────┘
          │  check-in a cada 30 min (7h–20h), expira em 48h
          ▼
   ┌──────────────┐
   │  RESPOSTA?   │
   └──┬────────┬──┘
 APROVADO   REFAZER
      │          │
      │          └─► pergunta na mesma thread:
      │               "ajustar o texto" ou "novo tema"
      │               └─► reentra no fluxo até aprovar
      ▼
 LinkedIn (claude_in_chrome) → agenda para 17:30 do dia seguinte
 → confirma por e-mail com screenshot → atualiza rodízio → commit
```

## Arquivos

```
bin/preflight.sh                      testa o egresso de rede e define o modo da execução
bin/contar.py                         reprova o texto fora dos limites do protocolo
bin/carrossel.py                      gera os PNGs 1080x1350 a partir do roteiro.json
bin/folha_contato.py                  folha de contato + base64 para anexar no e-mail
bin/roteiro.exemplo.json              modelo de roteiro, com os cinco tipos de slide

.claude/skills/linkedin-pipeline/     produção do conteúdo (etapas 1–6)
  SKILL.md                            orquestrador
  references/pesquisa.md              onde procurar, janela de 5 dias, formato do dossiê
  references/analise.md               critérios de pontuação e escolha da pauta
  references/redacao.md               tom, estrutura, o que nunca fazer, checagem
  references/criativo.md              carrossel, identidade visual, produção no Canva
  references/email.md                 envio, vocabulário de resposta, monitoramento
  references/publicacao.md            LinkedIn via browser + agendamento 17:30
  references/rotacao.md               regra do 4/2/2 e quando é legítimo furar
  templates/email_aprovacao.html      layout do e-mail

.claude/skills/linkedin-aprovacao/    segundo tempo: lê a resposta e dá seguimento
.claude/agents/                       pesquisador-fiscal, analista-pauta, roteirista-linkedin
estado/rodizio.json                   cota do mês e memória de temas
estado/publicacoes/                   um diretório por ciclo (texto, dossiê, slides, log)
estado/ESTRUTURA.md                   esquema do estado
```

## Agendamento

Routine **"LinkedIn — Produção de Conteúdo"**, cron `0 11 * * 1,3` (UTC) =
**segunda e quarta às 07:00** em Campo Grande (UTC-4). Cada disparo abre uma
sessão nova, que executa a skill `linkedin-pipeline`.

O monitoramento da resposta não é um cron: a própria sessão de produção agenda
seu retorno com `send_later` a cada 30 minutos, dentro da janela 7h–20h.

Pausar, editar horário ou apagar: peça ao Claude ("pausa a Routine do LinkedIn"),
ou use a lista de Routines da conta.

> Observação de calendário: o disparo é segunda e quarta, e a publicação sai
> terça e quinta às 17:30 — que era o par de dias mencionado no pedido original.
> O dia útil de intervalo é o que dá margem para a rodada de aprovação.

### Pendência: conectores da Routine

A Routine foi criada por ferramenta, e nesta organização o gatilho **não pôde
receber os conectores** — as sessões que ele dispara sobem sem `Gmail` e sem
`Canva`. Sem Gmail, o pipeline chega até o criativo e **não consegue enviar o
e-mail de aprovação**.

Para resolver, abra a Routine em **claude.ai → Routines**
(`LinkedIn — Produção de Conteúdo (seg/qua 07:00)`, id `trig_01WSnNxWZRN4G9pgPBYN7gv2`)
e anexe os conectores **Gmail** e **Canva** — opcionalmente **Jusratio**, que o
protocolo de pesquisa usa para jurisprudência. O restante da configuração
(horário, prompt, notificação) já está correto.

Enquanto isso não for feito, rode `/linkedin-pipeline` manualmente numa sessão
que tenha os conectores: o pipeline é o mesmo.

## Dependências

| Função | Ferramenta | Se faltar |
|---|---|---|
| Pesquisa | WebSearch | bloqueia o pipeline |
| Verificação em fonte primária | WebFetch + egresso liberado | cai em **modo degradado** (ver abaixo) |
| Jurisprudência | conector Jusratio | segue só com fonte normativa |
| Criativo | `bin/carrossel.py` + Chromium | bloqueia a etapa 5 |
| E-mail | conector Gmail | bloqueia o envio de aprovação |
| Publicação | skill `claude_in_chrome` | fallback `agent-browser` com sessão logada |

O Canva **não** entra no caminho do carrossel: nenhuma das duas ferramentas de
geração produz 5–8 slides em 4:5 sem um passo interativo. Detalhes e o teste que
mostrou isso estão em `references/criativo.md`.

## Rede: o que precisa estar liberado

O protocolo exige abrir a fonte primária antes de citar qualquer norma. Isso
depende da política de rede do environment (Claude Code on the web →
configuração do ambiente). Os domínios que o pipeline usa:

```
www.planalto.gov.br   www.in.gov.br            www.gov.br
www.cgibs.gov.br      portal.stf.jus.br        www.stj.jus.br
www.confaz.fazenda.gov.br
www.conjur.com.br     www.jota.info            www.migalhas.com.br
www.contabeis.com.br
```

`bash bin/preflight.sh` testa todos e imprime o modo da execução.

**Modo degradado** (menos de 3 fontes primárias alcançáveis): o pipeline não
trava, mas aperta o cinto — todo número de norma precisa de duas fontes
secundárias independentes, dados de fonte única não viram afirmação, julgamentos
sem confirmação saem da pauta, e o e-mail de aprovação abre com um aviso dizendo
o que não pôde ser verificado. As regras estão em `references/pesquisa.md`.

## Regras que o agente não quebra

- Uma execução produz **uma** publicação.
- Nada vai ao LinkedIn sem aprovação inequívoca por e-mail. Silêncio não é aval.
- Nenhuma norma é citada sem a fonte primária aberta e o número conferido.
- Sem pauta relevante na janela de 5 dias, ele não inventa: manda o e-mail
  explicando e propondo três temas perenes.
- Nunca digita credenciais do LinkedIn. Sessão deslogada = para e avisa.

## Rodar manualmente

```
/linkedin-pipeline          produz um pacote agora, fora do cronograma
/linkedin-aprovacao         checa a resposta e dá seguimento ao pacote pendente
```
