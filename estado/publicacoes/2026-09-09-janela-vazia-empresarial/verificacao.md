# Verificação de fontes primárias — tema perene "Recuperação judicial de cooperado produtor rural"

Executada em 2026-09-10, na produção de `texto.md` e `roteiro.json`.

## Tentativas de abertura de fonte primária (todas por WebFetch)

| URL tentada | Resultado |
|---|---|
| `planalto.gov.br/ccivil_03/leis/l8929.htm` (https) | 503 |
| `www.planalto.gov.br/ccivil_03/LEIS/L8929.htm` (http) | 503 |
| `planalto.gov.br/ccivil_03/leis/l11101.htm` | 503 |
| `planalto.gov.br/ccivil_03/leis/L11101compilado.htm` | 503 |
| `web.archive.org/web/.../l8929.htm` e `.../l11101.htm` | Ferramenta recusa domínio `web.archive.org` |
| `legis.senado.leg.br/norma/537831` | Bloqueado pelo proxy de egress (`EGRESS_BLOCKED`) |
| `www.jusbrasil.com.br/...` | Bloqueado pelo proxy de egress |
| `www.lexml.gov.br/urn/...` | Resolvido, mas o repositório não localizou o documento |
| `www.gov.br/planalto/pt-br` | Carrega, mas cai em captcha de verificação humana (confirma bloqueio, não dá acesso ao texto) |
| `www2.camara.leg.br/legin/...` (duas URLs, Lei 8.929 e Lei 11.101) | Bloqueado pelo proxy de egress |
| `www.conjur.com.br/...` (secundária, sobre CPR/penhor rural/RJ) | 403 |
| `www.migalhas.com.br/...` (secundária, mesmo tema) | 404 (URL não localizada) |
| `duckduckgo.com/html?q=...` | Bloqueado pelo proxy de egress |
| `www.stj.jus.br` | 403 |
| `www.gov.br/agricultura/pt-br` | Abriu normalmente (controle: confirma que nem todo `gov.br` está bloqueado, só os domínios específicos acima) |

## Conclusão

Nenhuma fonte primária (planalto.gov.br para Lei nº 8.929/1994 e Lei nº
11.101/2005) foi aberta nesta sessão. O padrão de bloqueio é o mesmo já
registrado em `dossie.md` do ciclo de 2026-09-09 para outras normas
(planalto.gov.br e bcb.gov.br "bloqueados", com captcha ou 503 confirmados por
WebFetch direto). Também não foi possível abrir nenhuma fonte secundária de
imprensa jurídica (Conjur, Migalhas, JusBrasil) nem mecanismo de busca
(DuckDuckGo) para corroborar por dupla fonte secundária, como foi feito para
outros achados do dossiê. Não há ferramenta de pesquisa jurisprudencial (STJ,
CourtListener, Jusratio) disponível nesta sessão apesar de instruções de
servidor MCP mencionarem essas capacidades: nenhuma function tool
correspondente foi de fato oferecida à sessão.

Os números de artigo citados no texto (Lei nº 8.929/1994, art. 3º; Lei nº
11.101/2005, art. 41, II e art. 49, caput e §3º) baseiam-se em conhecimento
jurídico consolidado sobre essas normas, amplamente citadas na doutrina e na
prática de recuperação judicial, e não em conferência direta da fonte
primária nesta sessão. Recomendo que a etapa de aprovação humana (Luis)
confirme esses números antes da publicação, ou que uma sessão futura com
acesso a `planalto.gov.br` refaça a checagem antes do post ir ao ar.
