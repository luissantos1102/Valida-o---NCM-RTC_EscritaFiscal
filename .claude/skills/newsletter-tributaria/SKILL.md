---
name: newsletter-tributaria
description: Produz a newsletter diária de Luis Santos sobre Direito Tributário, Reforma Tributária e Contabilidade (varredura das últimas 24h em fontes primárias e imprensa especializada, redação elaborada de 10-15 min de leitura) e envia por e-mail — sem fluxo de aprovação, é conteúdo de consumo próprio. Use quando a Routine "Newsletter Tributária — Produção Diária" disparar, ou quando o usuário pedir para "rodar a newsletter", "produzir a newsletter tributária" ou "mandar o resumo do dia".
---

# Newsletter diária — Tributário, Reforma Tributária e Contabilidade

Diferente do `linkedin-pipeline`, esta é **para consumo próprio de Luis Santos**,
não para publicação pública. Isso muda duas coisas: não há fluxo de aprovação —
o e-mail sai direto — e a cobertura é ampla (tudo que é relevante), não filtrada
por potencial de post.

Destinatário: **luis.santos@copasul.coop.br** (mesmo e-mail da rotina do LinkedIn).

## Execução

Rode as 3 etapas na ordem. Uma execução = um e-mail. Sempre termina com o envio
— mesmo em dia sem novidade, o e-mail curto de "dia tranquilo" conta como
conclusão do ciclo.

### 1. Pré-voo e pesquisar

Comece por `bash bin/preflight.sh` (mesmo script do pipeline do LinkedIn — cobre
as fontes primárias de tributário e, agora, `cfc.org.br` para contabilidade).
Depois siga `references/pesquisa.md`, inclusive a seção "Modo degradado" se o
pré-voo acusar bloqueio.

Janela: **últimas 24h**, contadas da data/hora de execução. Nada de recuar a
janela para "sempre ter conteúdo" — dia sem novidade normativa é informação
válida e vira o e-mail curto da seção 3.

### 2. Escrever

Siga `references/redacao.md` — inclusive a seção "Padrão validado" nele, que
registra o formato aprovado pelo usuário depois de duas rodadas de teste
visual. Resumindo o que não se negocia:

- **Prosa desenvolvida, não bullet duplo.** Cada item leva 3 a 5 parágrafos
  (o que aconteceu com detalhe técnico, por que importa na prática, o que vem
  a seguir/desdobramento). "O que mudou" + "Por que importa" em uma linha cada
  é insuficiente — já foi rejeitado uma vez por ser superficial.
- **Todo "Fonte" é link clicável de verdade**, com a URL real que você abriu
  ou que apareceu na busca — nunca só o nome do veículo sem `<a href>`. Marque
  o nível de verificação (`dupla/múltipla independente` ou `fonte única —
  tratar com cautela`) ao lado de cada link.
- **Extensão real de 10-15 min** — isso dá, em prosa técnica, algo entre
  1.800 e 2.800 palavras visíveis (conte com um `<[^>]+>` strip antes de
  enviar, se tiver como). Não estufe artificialmente; construa isso tendo
  itens suficientes (normalmente 2 por eixo) escritos com profundidade, mais
  um parágrafo de abertura editorial e um parágrafo de fechamento ("Para
  fechar") amarrando os achados do dia.
- **Elementos visuais reais**, não só cor de fundo: use o banner
  `estado/newsletter/assets/hero.png` no topo e os selos
  `icon-tributario.png` / `icon-reforma.png` / `icon-contabilidade.png` ao
  lado do título de cada seção — todos hospedados via
  `https://raw.githubusercontent.com/luissantos1102/Valida-o---NCM-RTC_EscritaFiscal/refs/heads/claude/linkedin-content-agent-7hnba3/estado/newsletter/assets/<arquivo>`.
  Esses assets são estáticos (sem data), reaproveite-os todo dia — só
  regenere se quiser mudar o design (script de referência: renderize um HTML
  com a paleta de `bin/temas.py` via `headless_shell` do Chromium, como feito
  na criação original, documentada no histórico do pacote de testes).

Antes de escrever, leia `estado/newsletter/enviados.json` — não repita, como
item novo, algo já coberto nos últimos 7 dias. Se o mesmo fato voltar por ter
ganhado desdobramento (ex.: um projeto virou norma), trate como atualização,
não como novidade, e diga isso explicitamente ("como cobrimos em DD/MM...").

### 3. Enviar

Monte o e-mail com `templates/email_newsletter.html` (cartão HTML em tabelas,
paleta marinho/âmbar, banner e selos — mesmo padrão validado no teste visual).
Assunto:

```
Newsletter Tributária — <AAAA-MM-DD>
```

Envie via `mcp__Gmail__send_message` direto para luis.santos@copasul.coop.br —
**sem esperar resposta, sem fluxo de aprovação**. Depois:

1. Acrescente uma linha em `estado/newsletter/log.md`: data/hora, quantos itens,
   eixos cobertos, se saiu em modo completo ou degradado.
2. Atualize `estado/newsletter/enviados.json` com os itens novos desta edição
   (título curto + data + fonte), removendo entradas com mais de 7 dias.
3. Commite e faça push no branch de trabalho.

Não agende monitoramento de resposta — esta skill não tem ciclo de aprovação,
encerra no envio.

## Dia sem novidade

Se a varredura de 24h não encontrar nenhum fato normativo novo nos três eixos,
não force pauta. Envie um e-mail curto avisando o dia tranquilo, com no máximo
um parágrafo de contexto (ex.: "nada publicado nas últimas 24h; o radar segue
em: <2-3 itens pendentes de regulamentação a acompanhar>"). Isso conta como
edição enviada — registre e feche o ciclo normalmente.

## Invariantes

- Uma execução = um e-mail. Nunca envie duas edições no mesmo dia.
- Toda afirmação normativa carrega a fonte (número, órgão, data), no nível de
  verificação que o ambiente permitiu — em modo degradado, o e-mail abre
  avisando isso.
- Sem fluxo de aprovação: o conteúdo vai direto ao e-mail. Não invente fluxo de
  aprovação nem espere resposta do usuário para considerar o ciclo concluído.
- Se `AVISO=SEM_PERSISTENCIA` aparecer no pré-voo, avise no rodapé do e-mail:
  o dedup de 7 dias pode repetir itens até a persistência ser corrigida
  (repositório em "Select repositories" na configuração da Routine).
