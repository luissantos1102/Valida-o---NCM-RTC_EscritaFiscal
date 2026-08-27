# Publicação no LinkedIn

**Só execute este arquivo depois de uma aprovação inequívoca por e-mail.**

Meta: publicar exatamente no horário combinado com o usuário (normalmente
17:30 do dia seguinte ao disparo, Campo Grande UTC-4).

## Como funciona

Publicação é via **API oficial do LinkedIn** (`bin/publicar_linkedin.py`), não
navegador. Isso muda um conceito importante: a API **não tem agendamento
nativo** — ela publica na hora em que é chamada. Não há isso a simular.
**A própria Routine, ao chamar o script no horário certo, já é o agendamento.**
Se o horário combinado ainda não chegou, agende um `send_later`/check-in para
aquele momento em vez de tentar "marcar" a publicação para depois.

Formato do carrossel: **multi-imagem PNG**, não Documento/PDF — decisão do
usuário, que já verificou engajamento melhor nesse formato. Usa os mesmos PNGs
que `bin/carrossel.py` gera, sem conversão nenhuma.

## Pré-requisitos (variáveis de ambiente)

```
LINKEDIN_ACCESS_TOKEN
LINKEDIN_PERSON_URN
```

Configuradas em **Environment variables** da Routine (nunca no repositório).
Se estiverem ausentes ou a API responder 401, **pare** — não há como publicar
sem elas. Avise por e-mail na mesma thread, no formato de
`references/email.md`, pedindo que o usuário rode `bin/linkedin_oauth.py`
novamente (o token dura cerca de 60 dias) e reagende o check-in.

## Passos

1. Confira que o pacote está aprovado e que o horário de publicação chegou
   (ou está a poucos minutos — não adiante a publicação).
2. Rode primeiro em modo seguro:
   ```
   python3 bin/publicar_linkedin.py estado/publicacoes/<AAAA-MM-DD>-<slug> --dry-run
   ```
   Confira o `commentary` no JSON impresso contra `texto.md` — precisa ser
   idêntico, incluindo hashtags. Confira a contagem de imagens contra o
   número de slides do pacote.
3. Se o dry-run bater, publique de verdade:
   ```
   python3 bin/publicar_linkedin.py estado/publicacoes/<AAAA-MM-DD>-<slug>
   ```
4. O script grava `<pacote>/comprovante/resposta_api.json` com o `post_urn` e
   a resposta da API. Confira que `post_urn` não veio vazio.
5. Se a API responder erro (qualquer status fora de 200/201), o script para e
   imprime o corpo do erro. Não tente contornar por conta própria: leia o
   erro, e se não for auto-explicativo (token expirado, escopo faltando),
   avise por e-mail com o erro literal e pare.

## Verificação obrigatória antes de confirmar sucesso

- [ ] `post_urn` presente e não vazio em `resposta_api.json`.
- [ ] Número de imagens enviadas bate com o número de slides do pacote.
- [ ] `commentary` no dry-run era idêntico a `texto.md`.

## Fechamento do ciclo

1. Responda na thread do e-mail confirmando: publicado, com o `post_urn` e o
   link (`https://www.linkedin.com/feed/update/<post_urn>/`).
2. Atualize `estado/rodizio.json`: incremente a cota do eixo, grave o template
   usado em `ultimo_template`, e acrescente ao `historico` (data, eixo, tema,
   slug, template, post_urn).
3. Grave `status: "publicado"` e a data/hora em `estado/publicacoes/<...>/meta.json`.
4. Commite e faça push no branch de trabalho — **inclusive** `comprovante/resposta_api.json`.
5. Encerre. Não agende mais check-ins para este pacote.

## Nunca

- Nunca commite `LINKEDIN_ACCESS_TOKEN` nem `LINKEDIN_PERSON_URN` em nenhum
  arquivo do repositório.
- Nunca tente login por navegador como alternativa — essa via foi abandonada
  (sessão cloud efêmera não carrega login de nenhum dispositivo do usuário;
  ver `docs/ATIVACAO.md`).
- Nunca publique sem o dry-run ter sido conferido primeiro nesta mesma execução.
