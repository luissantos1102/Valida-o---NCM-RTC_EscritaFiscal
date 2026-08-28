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
  cfc.org.br               # Conselho Federal de Contabilidade — NBCs
)
IMPRENSA=(
  www.conjur.com.br
  www.jota.info
  www.migalhas.com.br
  www.contabeis.com.br
  valor.globo.com
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

echo "== Persistência do estado =="
# O rodízio 4/2/2 e o histórico de temas só sobrevivem se o push funcionar:
# o container é reciclado no fim da sessão. Descobrir isso no fim custa a
# execução inteira, então testamos antes de pesquisar.
BR=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if git push --dry-run origin "$BR" >/dev/null 2>&1; then
  echo "  OK        push para origin/$BR"
  PUSH_OK=1
else
  echo "  BLOQUEADO push para origin/$BR"
  echo "            O repositório provavelmente não está em 'Select repositories'"
  echo "            na Routine. Sem isso o estado do rodízio não persiste."
  PUSH_OK=0
fi

echo
if [ "$PUSH_OK" -eq 0 ]; then
  echo "AVISO=SEM_PERSISTENCIA"
  echo "Siga a execução, mas anexe rodizio.json ao e-mail de aprovação e diga ao"
  echo "usuário que a cota do mês precisa ser reaplicada à mão."
  echo
fi

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
