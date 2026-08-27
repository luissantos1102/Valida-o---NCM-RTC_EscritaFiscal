#!/usr/bin/env bash
# Verifica, antes de pesquisar, o que este ambiente consegue alcançar.
# Uso: bash bin/preflight.sh
# Saída: um relatório e o MODO de operação da execução.

set -uo pipefail

PRIMARIAS=(
  www.planalto.gov.br      # leis e LCs
  www.in.gov.br            # DOU
  www.gov.br               # Receita Federal, Fazenda
  www.cgibs.gov.br         # Comitê Gestor do IBS
  portal.stf.jus.br
  www.stj.jus.br
  www.confaz.fazenda.gov.br
)
IMPRENSA=(
  www.conjur.com.br
  www.jota.info
  www.migalhas.com.br
  www.contabeis.com.br
)

testa() {
  curl -s -o /dev/null -w "%{http_code}" --max-time 12 "https://$1/" 2>/dev/null
}

ok_p=0; ok_i=0
echo "== Fontes primárias =="
for d in "${PRIMARIAS[@]}"; do
  c=$(testa "$d")
  if [[ "$c" =~ ^(2|3) ]]; then echo "  OK       $d"; ok_p=$((ok_p+1))
  else echo "  BLOQUEADO $d  (http=$c)"; fi
done

echo "== Imprensa especializada =="
for d in "${IMPRENSA[@]}"; do
  c=$(testa "$d")
  if [[ "$c" =~ ^(2|3) ]]; then echo "  OK       $d"; ok_i=$((ok_i+1))
  else echo "  BLOQUEADO $d  (http=$c)"; fi
done

echo
if [ "$ok_p" -ge 3 ]; then
  echo "MODO=COMPLETO"
  echo "Verifique cada norma na fonte primária, como manda o protocolo."
else
  echo "MODO=DEGRADADO"
  echo "Egresso bloqueado para fonte primária ($ok_p de ${#PRIMARIAS[@]} alcançáveis)."
  echo "Siga as regras do modo degradado em references/pesquisa.md antes de escrever."
  echo "Avise o usuário: a correção é liberar estes domínios na política de rede"
  echo "do ambiente (Claude Code on the web → configuração do environment)."
fi
