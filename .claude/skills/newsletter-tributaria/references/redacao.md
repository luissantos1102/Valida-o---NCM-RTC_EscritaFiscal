# Papel: redator da newsletter

## Padrão validado (não regredir)

A primeira rodada de teste visual saiu superficial demais e foi rejeitada:
bullets de uma linha, sem link de fonte, sem elementos visuais reais e bem
abaixo dos 10-15 min prometidos. A segunda rodada corrigiu isso e foi
aprovada como padrão. Ao escrever cada edição, mire nisto:

- Cada item de eixo tem **3 a 5 parágrafos** (não duas linhas): o fato com
  detalhe técnico (número de acórdão/norma, artigo, data), um parágrafo
  "E na prática, o que muda para a Copasul", e um parágrafo de
  desdobramento/contexto ("o que vem agora", histórico, ou ressalva de
  verificação quando a fonte for única).
- Toda fonte é **link `<a href="URL">` de verdade**, com a URL real —
  encontrada na busca ou aberta via WebFetch — e uma etiqueta explícita do
  nível de verificação (dupla/múltipla fonte independente, ou fonte única a
  tratar com cautela).
- A edição abre com um **parágrafo editorial curto** (não só a lista de
  bullets) amarrando o fio do dia, e fecha com um parágrafo **"Para fechar"**
  de síntese antes do Radar — é isso que dá corpo analítico à newsletter, não
  só lista de fatos soltos.
- Elementos visuais reais no e-mail, mas **sem nenhuma tag `<img>`** (ela é
  removida no envio, testado e confirmado — ver `SKILL.md`): faixa de cor no
  topo/rodapé e um selo circular em CSS puro (div + `border-radius` +
  `background-color` + letra) ao lado do título de cada seção de eixo. Use
  sempre `background-color`, nunca `background` (também removida no envio).
  O template já implementa isso — só troque a letra do selo por eixo.
- **Parágrafos justificados** (`text-align:justify` no `<td>`/`<div>` do
  corpo), não alinhados à esquerda — apontado pelo usuário na auditoria de
  2026-08-28. O template já aplica isso; mantenha em qualquer edição manual.
- **Paleta Copasul, não a paleta do LinkedIn.** A partir da auditoria de
  2026-08-28, a newsletter usa cores e fonte próprias (verde Copasul/âmbar,
  Arial) — diferente do carrossel do LinkedIn (marinho/âmbar, Georgia). Ver
  a paleta completa e a justificativa no cabeçalho de
  `templates/email_newsletter.html`. Não volte a copiar `bin/temas.py` aqui.
- **Zero travessão (—), nem "com moderação".** A régua inicial de "no
  máximo 1 a cada 2-3 parágrafos" não bastou, é proibição total desde
  2026-08-28. Troque por ponto, vírgula, dois-pontos, parênteses ou
  conectivo.

### Histórico de layout (rodadas 1 a 5, todas superadas)

No mesmo dia (2026-08-28), o layout visual passou por cinco rodadas antes
de chegar ao padrão definitivo (ver seção seguinte): cartão escuro
marinho/verde (rejeitado, "não consegui gostar"), cartão sóbrio cinza
`#D9D9D9`/branco no estilo dos sistemas internos Copasul, o mesmo cartão
com o cinza movido para o próprio cartão e texto mais grosso, um layout
baseado num e-mail real de comunicação interna da Copasul ("Pílula do
Compliance") com caixa verde escura por item, e por fim um cartão
`#F9F9F9` com corpo em serifa ("Editorial + Cartão leve"). Nenhuma
sobreviveu ao próprio dia. Não implemente nenhuma delas — ficam registradas
só para não serem repetidas por engano. O padrão atual é o da seção
abaixo.

## Padrão definitivo de layout (verde Copasul sobre a edição real)

O que finalmente convenceu não veio de mais uma rodada de teste visual: o
usuário comparou a 1ª edição de produção real do dia (enviada de manhã,
ainda no template marinho/âmbar herdado do LinkedIn, thread
`1a047e917f5d0c36`) com uma vitrine de referências de newsletter fora do
projeto, e pediu para recriar aquele e-mail real trocando só o azul
profundo do fundo do cartão pelo verde Copasul. A partir daí vieram
ajustes sucessivos de escrita e tipografia:

- **Fundo do cartão em `#013220`** (verde Copasul mais escuro), sobre
  página branca. Painéis internos (aviso, fontes) em `#1B5E42` com borda
  `#2F8C63`; era azul marinho no e-mail original, só a cor mudou.
- **Fonte: Arial em tudo**, com uma única exceção: o título grande do
  cabeçalho ("Direito Tributário · Reforma Tributária · Contabilidade")
  fica em Georgia/serifa, a pedido explícito do usuário. Não generalize a
  serifa para o resto do template.
- **Texto de corpo em `#F2F5F8` (quase-branco)**, não um cinza apagado: o
  usuário já pediu essa troca uma vez por ficar "meio apagado" contra o
  verde escuro.
- **Item em prosa corrida, sem caixa no corpo** (mesmo espírito da rodada
  "Editorial" anterior); só os painéis de aviso e fontes têm caixa
  (`#1B5E42`, texto `#D7E9DE` para contraste).
- **"E na prática, o que muda para a Copasul:"** é uma linha própria, 16px,
  negrito, âmbar, em CAIXA ALTA, antes do parágrafo explicativo. Não é mais
  itálico embutido no meio do texto.
- **Destaques de dado-chave no corpo** (valores, prazos, números de
  norma/acórdão) em `<strong style="color:#D6A544;">` (âmbar), replicando o
  negrito que já existia no e-mail real de origem.
- **Título de cada eixo** (ao lado do selo, ex. "Direito Tributário") em
  17px negrito âmbar, bem mais destacado que um kicker comum.
- **Selo em 40px** com borda âmbar e fundo `#1B5E42`, letra âmbar (não o
  selo pequeno de 22px da rodada "Editorial").
- **Cartão em 890px** (não 660, 840 nem outra largura de rodadas
  anteriores).
- **Nenhum domínio como texto puro.** Ver a regra 6 no cabeçalho de
  `templates/email_newsletter.html`: o Gmail autolinkifica menções de
  domínio em texto puro com o azul padrão dele, ilegível sobre fundo
  escuro. Toda menção de domínio, mesmo dentro do aviso de modo degradado,
  precisa ser `<a href="https://...">` com `color:#D6A544` explícito.

O template já implementa tudo isso; siga a estrutura dele item por item, e
não reintroduza nenhum elemento das rodadas 1 a 5 (cartão `#F9F9F9`, caixa
verde no corpo do item, faixa verde no Radar, corpo inteiro em serifa,
domínio como texto puro) sem o usuário pedir de novo explicitamente.

Tom: informativo e analítico, como um boletim editorial de escritório
especializado — mais formal que o post de LinkedIn, sem precisar da abertura
"gancho" de rede social. O leitor já abriu o e-mail porque quer o resumo; vá
direto ao conteúdo.

Público: o próprio Luis Santos — estudante de Direito, atua no fiscal/contábil
de uma cooperativa agrícola como Key User de Oracle EBS. Pode usar termos
técnicos sem explicar o básico, mas sempre que citar uma norma dê contexto
suficiente para entender a mudança sem abrir a fonte.

## Tamanho e formato

10 a 15 minutos de leitura (aproximadamente 1.800 a 2.800 palavras, variando
com o volume do dia — não estufe um dia fraco para bater a meta).

Estrutura fixa:

```
1. Resumo executivo (5-8 bullets, uma linha cada — para quem só vai ler isso)
2. Direito Tributário
3. Reforma Tributária (IBS/CBS)
4. Contabilidade
5. Radar (opcional) — o que está para acontecer nos próximos dias/semanas
   (prazos, votações previstas, prazos de vigência) e vale acompanhar
```

Eixo sem novidade no dia: omita a seção, não escreva "nada a reportar" —
o resumo executivo já cobre isso implicitamente por ausência.

## Por item, dentro de cada eixo

```
### <título curto do fato>

**O que mudou:** 1-2 frases, direto ao ponto.

**E na prática, o que muda para a Copasul:** o efeito prático, ancorado na
operação real — fiscal, Oracle EBS, cadastro de item, apuração, crédito do
adquirente. Pode ficar em "sem efeito prático direto para a Copasul hoje,
mas..." quando for o caso; não force o ângulo cooperativista onde ele não
existe, mas procure-o antes de descartar.

**Fonte:** identificação normativa + link.
```

Itens marcados como `projeto_proposta` levam a etiqueta **[projeto]** antes do
título — nunca apresente proposta como se fosse norma vigente.

## O que evitar

- Não repita, como novidade, item já coberto (ver `enviados.json`) sem
  desdobramento real.
- Não force ângulo prático onde não há — "sem efeito prático imediato" é uma
  frase válida.
- Não abra com floreio nem peça desculpa por dia fraco; vá ao resumo executivo.
- Não invente fonte. Se o achado só tem fonte secundária única, ou não entra,
  ou entra qualificado como não confirmado (ver modo degradado em
  `pesquisa.md`).
- **Usar travessão.** Proibido, sem exceção. Apontado pelo usuário como
  problema real na auditoria de 2026-08-28, e depois de ver que "no máximo 1
  a cada 2-3 parágrafos" não bastou, a régua virou zero. É a marca mais
  visível de texto gerado por IA. Resolva com ponto final, vírgula,
  dois-pontos, parênteses ou um conectivo. Ao revisar, procure "—" no texto
  pronto: qualquer ocorrência, reescreva antes de enviar.

## Dia sem novidade

Substitua toda a estrutura por:

```
Nada de novo com consequência jurídica ou contábil nas últimas 24h nos três
eixos. Radar para os próximos dias: <1-3 itens pendentes, uma linha cada>.
```
