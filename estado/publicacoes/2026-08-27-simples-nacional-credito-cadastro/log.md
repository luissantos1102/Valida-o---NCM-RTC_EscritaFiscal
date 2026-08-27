# Log

- **2026-08-27** — Execução de teste original (modo degradado, texto com desvio
  operacional). Nunca enviado para aprovação.
- **2026-08-27 (refeitura)** — A pedido do usuário ("gostei do tema Simples
  Nacional, refaça"), o texto foi reescrito para o eixo jurídico: a questão em
  aberto passou a ser "o crédito se refaz retroativamente ou fica preservado
  quando o fornecedor muda de regime", com posição fundamentada na não
  cumulatividade plena da LC 214/2025. Carrossel regerado no template
  `editorial` (nova identidade visual, âmbar/marinho). 1.757 caracteres,
  aprovado em `bin/contar.py`.
- **2026-08-27** — E-mail de aprovação enviado. thread_id=1a043206b241f6ea. Status:
  aguardando_aprovacao. Check-in agendado para 30 min.
- **2026-08-27 12:23 UTC** — Resposta do usuário na thread: "Aprovado com ajustes
  <Data da publicação deve ser 27/08/2026 às 17:30>". Classificado como
  **Aprovado com ajuste** — o ajuste é só a data (hoje, não amanhã). Texto e
  criativo não mudam. Aplicado: data_agendamento → 2026-08-27T17:30:00-04:00.
  Seguindo direto para publicacao.md, sem novo aval.
- **2026-08-27 12:46 UTC** — Tentativa de publicação. Nem `claude_in_chrome` nem
  `agent-browser` (não instalado) resolvem: sessão cloud efêmera não carrega
  sessão do LinkedIn logada de nenhum dispositivo. Protocolo seguido: nunca
  digitar credenciais. Avisado por e-mail na mesma thread pedindo login manual
  no ambiente de automação, com prazo até 17:30 de hoje. status →
  aprovado_bloqueado_login_linkedin. Check-in reagendado para 30 min.
- **2026-08-27 12:5x UTC** — Decisão do usuário: investigar a API oficial do
  LinkedIn em vez de sessão de browser. Pesquisado: "Share on LinkedIn" +
  w_member_social é self-serve, sem revisão, serve para perfil pessoal (ao
  contrário da Community Management API, que exige CNPJ). Carrossel = post de
  Documento (PDF), 1080x1350 já é o formato recomendado. Token de acesso padrão
  dura 60 dias sem refresh automático — reautorização manual periódica. Sem
  agendamento nativo na API: a própria Routine, ao chamar a API às 17:30, FAZ o
  agendamento — não precisa simular o botão do LinkedIn.
  Implementação não cabe a tempo do slot de hoje (17:30). Publicação manual
  recomendada para esta rodada, via e-mail. status →
  aprovado_publicacao_manual_recomendada.
- **2026-08-27 13:22 UTC** — Check-in: sem resposta nova do usuário além da
  própria atualização de status enviada às 13:19 UTC. Nada a fazer além de
  reagendar. status mantido: aprovado_publicacao_manual_recomendada.
- **2026-08-27 13:53 UTC** — Check-in: sem resposta nova na thread. Integração
  via API construída e testada em --dry-run nesta janela, mas ainda sem
  LINKEDIN_ACCESS_TOKEN/LINKEDIN_PERSON_URN (aguardando o usuário criar o app e
  passar Client ID/Secret). Publicação manual de hoje segue como recomendação
  vigente. status mantido: aprovado_publicacao_manual_recomendada. Reagendado.
