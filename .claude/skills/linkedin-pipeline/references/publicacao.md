# Publicação no LinkedIn

**Só execute este arquivo depois de uma aprovação inequívoca por e-mail.**

Meta: post agendado para **17:30 do dia seguinte ao disparo** (horário de
Campo Grande, UTC-4). Se o disparo foi segunda, agenda para terça 17:30;
se foi quarta, para quinta 17:30.

## Ferramenta

Use a skill **`claude_in_chrome`** — ela opera o Chrome já logado, o que evita
login automatizado e o risco de bloqueio de sessão. Se ela não estiver
disponível no ambiente, use a skill `agent-browser` sobre um perfil de Chrome
com a sessão do LinkedIn já autenticada.

Nunca digite credenciais do LinkedIn. Se a sessão estiver deslogada, **pare**,
avise por e-mail na mesma thread pedindo que o login seja feito manualmente, e
reagende o check-in. Publicação perdida se recupera; conta bloqueada, não.

## Passos

1. Abra `https://www.linkedin.com/feed/` e confirme que está logado como Luis Santos.
2. Clique em **Começar publicação** / *Start a post*.
3. Cole o texto aprovado **exatamente** como está no pacote. Depois de colar,
   releia na tela: o LinkedIn às vezes come quebras de linha e junta parágrafos.
   Corrija a formatação até bater com o original.
4. Anexe o criativo:
   - carrossel → adicione os PNGs em ordem (`slide-01.png` … `slide-0N.png`) e
     **confira a ordem na pré-visualização**;
   - imagem única → anexe o PNG.
5. Se o pacote indicar link para o primeiro comentário, guarde-o para depois do
   agendamento (o LinkedIn não permite comentar antes de publicar — registre no
   log que ficou pendente e comente quando o post for ao ar).
6. Clique no **ícone de relógio** (agendar), ao lado de *Publicar*.
7. Defina data = dia seguinte ao disparo, hora = **17:30**. Confira o fuso
   mostrado pelo LinkedIn; se ele exibir outro fuso, converta para que o post
   saia às 17:30 em Campo Grande (UTC-4).
8. Confirme em **Agendar**.
9. Tire um screenshot da confirmação e da tela de posts agendados
   (`Publicar` → *Ver todos os posts agendados*). Salve em
   `estado/publicacoes/<AAAA-MM-DD>-<slug>/comprovante/`.

## Verificação obrigatória antes de confirmar

- [ ] Texto na tela idêntico ao aprovado (inclusive parágrafos e hashtags).
- [ ] Slides na ordem certa na pré-visualização.
- [ ] Data e hora conferidas no fuso correto.
- [ ] Perfil correto (conta pessoal, não página de empresa).

Se qualquer item falhar, não confirme. Corrija; se não conseguir, salve o
rascunho, avise por e-mail e pare.

## Fechamento do ciclo

1. Responda na thread do e-mail confirmando: post agendado, data/hora, com o
   screenshot anexado.
2. Atualize `estado/rodizio.json`: incremente a cota do eixo, grave o template
   usado em `ultimo_template`, e acrescente ao `historico` (data, eixo, tema,
   slug, template, URL/ID do post se disponível).
3. Grave `status: "agendado"` e a data/hora em `estado/publicacoes/<...>/meta.json`.
4. Commite e faça push no branch de trabalho.
5. Encerre. Não agende mais check-ins para este pacote.
