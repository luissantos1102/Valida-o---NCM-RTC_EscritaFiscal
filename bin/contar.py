#!/usr/bin/env python3
"""Confere o texto da publicação contra os limites do protocolo.

Uso: python3 bin/contar.py <pacote>/texto.md
"""
import io
import re
import sys

MIN, ALVO, MAX, TETO_LINKEDIN = 1300, 1800, 1900, 3000

if len(sys.argv) != 2:
    sys.exit(__doc__)

t = io.open(sys.argv[1], encoding="utf-8").read().strip()
n = len(t)
pars = [p for p in t.split("\n\n") if p.strip()]
tags = re.findall(r"#\w+", t)
longos = [i + 1 for i, p in enumerate(pars) if len(p) > 400]

print(f"caracteres : {n}   (mire {ALVO}; faixa {MIN}-{MAX}; teto do LinkedIn {TETO_LINKEDIN})")
print(f"parágrafos : {len(pars)}")
print(f"hashtags   : {len(tags)}  {' '.join(tags)}")

erros = []
if n > MAX:
    erros.append(f"{n - MAX} caracteres acima do teto — corte antes de seguir.")
elif n > ALVO:
    print(f"aviso     : {n - ALVO} caracteres acima do alvo de {ALVO}. "
          "Passa, mas sem folga para revisão.")
if n < MIN:
    erros.append(f"{MIN - n} caracteres abaixo do alvo — o texto está raso.")
if not 3 <= len(tags) <= 5:
    erros.append(f"{len(tags)} hashtags — o protocolo pede de 3 a 5.")
if "Fontes:" not in t:
    erros.append("falta o bloco 'Fontes:' no fim.")
if longos:
    erros.append(f"parágrafo(s) {longos} passam de 400 caracteres — quebre.")
if re.search(r"https?://", t):
    erros.append("há link no corpo do post — leve para o primeiro comentário.")

print()
if erros:
    print("REPROVADO:")
    for e in erros:
        print(f"  - {e}")
    sys.exit(1)
print("APROVADO nos limites mecânicos. Falta a checagem editorial da redacao.md.")
