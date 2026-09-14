# Dossiê de pesquisa — ciclo 2026-09-14 (janela 2026-09-09 a 2026-09-14)

Pré-voo (`bin/preflight.sh`): `MODO=COMPLETO` no agregado, mas com bloqueios
pontuais confirmados por teste direto (curl/WebFetch): `www.planalto.gov.br`,
`www.in.gov.br`, `portal.stf.jus.br`, `www.stj.jus.br` (403),
`www.confaz.fazenda.gov.br`, `www.conjur.com.br` bloqueados; `www.gov.br`,
`www.cgibs.gov.br`, `cfc.org.br`, `www.jota.info`, `www.migalhas.com.br`,
`www.contabeis.com.br`, `valor.globo.com` acessíveis no agregado. Na varredura
efetiva, também ficaram bloqueados ou indisponíveis: `www.bcb.gov.br`,
`www.camara.leg.br`, `nfe.fazenda.gov.br` (503), e a maior parte dos veículos
especializados em agro/cooperativismo (OCB, Mundo Coop, Canal Rural,
AgroRevenda, Análise, Sovos, Synchro), além de `Dizer o Direito` e `Jusbrasil`.

## Achados

### [TRIBUTÁRIO]

1. **Ato Conjunto RFB/CGIBS adia validação da rejeição 1115 da NF-e (IBS/CBS); preenchimento dos campos continua obrigatório.**
   Data: 12/09/2026. `verificacao: unica_secundaria` (Portal Contábeis,
   https://www.contabeis.com.br/noticias/79337/). Número do Ato Conjunto e da
   Nota Técnica 2025.002 v.1.51 NÃO conferidos em fonte primária
   (`nfe.fazenda.gov.br` respondeu 503; `in.gov.br`/`planalto.gov.br`
   bloqueados).

2. **STJ (repetitivo, "Tema 1276" segundo a matéria): CPRB não pode ser excluída da base de PIS/Cofins.**
   Data: 11/09/2026. `verificacao: unica_secundaria` (Portal Contábeis citando
   Valor Econômico, https://www.contabeis.com.br/noticias/79365/). Número do
   REsp/Tema não conferido (`stj.jus.br` bloqueado, 403).

3. **STJ nega mandado de segurança coletivo para excluir benefício de ICMS da base de IRPJ/CSLL (REsp 2.255.283, 2ª Turma).**
   Data: 10/09/2026. `verificacao: unica_secundaria` (Portal Contábeis,
   https://www.contabeis.com.br/noticias/79331/). Número do REsp não
   conferido.

4. **PL 3.186/2026: parcelamento de débitos com a União em até 240 meses, descontos de até 100% em multa/juros.**
   Data: 11/09/2026 (tramitação). `verificacao: unica_secundaria`
   (https://www.contabeis.com.br/noticias/79353/). É **projeto**, não lei
   vigente — `camara.leg.br` bloqueado, sem confirmação de andamento.

5. **[baixa confiança] "LC 236/26" alteraria art. 142 do CTN com teto de multa tributária (75/100/150%).**
   Data da matéria: 11/09/2026. `verificacao: unica_secundaria`, fonte única
   e de opinião (Migalhas, https://www.migalhas.com.br/depeso/464038/), sem
   segunda fonte encontrada apesar de tentativa em Contábeis, JOTA, Congresso
   em Foco e Câmara. Status indeterminado (sancionada ou não).

### [EMPRESARIAL]

6. **Prazo para cooperativas optarem pelo regime específico do ato cooperativo na Reforma Tributária corre até 31/10/2026 (janela aberta em 01/09/2026).**
   Fato-âncora: o **prazo em curso**. Base legal consolidada: regime opcional
   do ato cooperativo na LC 214/2025; regulamentação por decreto cujo número
   ("Decreto nº 12.955/2026", citado por fontes secundárias) NÃO foi
   confirmado em fonte primária. `verificacao: dupla_secundaria` (Mundo Coop e
   materiais institucionais Somos Cooperativismo, fontes distintas,
   convergem no prazo e no número do decreto, mas nenhuma página foi aberta
   por completo — acesso bloqueado nesta sessão).

### [CONTRATUAL]

Nenhum achado com fato normativo por âncora dentro da janela de 5 dias.
Descartado por falta de âncora: estatística de mercado sobre recorde de
recuperações judiciais no agro (RGF Consultoria, sem norma associada); carta-
manifesto de 98 empresários pró-Reforma Tributária (11/09, não reage a norma
identificável); artigo doutrinário geral sobre conflito de interesses/partes
relacionadas (Migalhas, 14/09, sem norma nova).

### Descartados por falta de verificação (não chegaram a candidatos)

- CFOPs 1.949/2.949 (Portal Contábeis, 11/09, formato podcast) — conteúdo não
  aberto por completo, ato normativo por trás não identificado.
- Resolução CMN 5.340/2026 (crédito rural/garantias) — fora da janela de 5
  dias nesta rodada (fato de 04/09/2026), sem desdobramento novo.

## Aplicação do filtro de analise.md (critério b — fonte primária verificada)

Nenhum dos 6 candidatos acima tem `verificacao: primaria`. Sob a regra fixada
para esta execução — **"nenhuma norma citada sem a fonte primária aberta e
conferida"** —, todos são descartados pelo critério (b) do filtro inicial de
`analise.md`, inclusive o candidato 6 (empresarial), que teria dupla fonte
secundária independente e seria, por mérito jurídico, o mais forte do ciclo
(prazo real em curso, tensão jurídica identificável, eixo em dívida). Análise
completa feita pelo agente `analista-pauta`, confirmando a ausência de
sobreviventes ao filtro.

**Conclusão: janela vazia nesta execução, para os três eixos.** Nenhuma pauta
publicável nos moldes exigidos.
