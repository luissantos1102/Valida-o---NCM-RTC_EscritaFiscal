#!/usr/bin/env python3
"""Autorização OAuth do app do LinkedIn — roda uma vez a cada ~60 dias.

Uso:
    # 1. Gera o link de autorização (você abre no navegador e loga)
    python3 bin/linkedin_oauth.py auth-url --client-id SEU_CLIENT_ID

    # 2. Depois de autorizar, o LinkedIn redireciona para uma página que não
    #    carrega (é esperado — não há servidor ali). Copie a URL inteira da
    #    barra de endereço e cole abaixo.
    python3 bin/linkedin_oauth.py exchange --client-id ID --client-secret SECRET \
        --redirect-url "http://localhost:8000/callback?code=...&state=..."

O passo 2 imprime as variáveis prontas para colar em Environment variables da
Routine: LINKEDIN_ACCESS_TOKEN, LINKEDIN_PERSON_URN, LINKEDIN_TOKEN_EXPIRA_EM.

Nunca commite essas variáveis no repositório. Elas vivem só na configuração
da Routine (claude.ai/code/routines → editar → ícone de nuvem → ambiente).
"""
import argparse
import secrets
import sys
import urllib.parse

import requests

REDIRECT_URI_PADRAO = "http://localhost:8000/callback"
SCOPES = "openid profile w_member_social"


def auth_url(client_id, redirect_uri):
    state = secrets.token_urlsafe(16)
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "state": state,
    }
    url = "https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode(params)
    print("Abra este link no navegador ONDE VOCÊ JÁ ESTÁ LOGADO no LinkedIn:\n")
    print(url)
    print(f"\nRedirect URI usado: {redirect_uri}")
    print("(precisa ser exatamente o mesmo cadastrado na aba Auth do app)")
    print(f"\nstate gerado (não é necessário guardar, é só anti-CSRF): {state}")


def exchange(client_id, client_secret, redirect_url, redirect_uri):
    parsed = urllib.parse.urlparse(redirect_url)
    qs = urllib.parse.parse_qs(parsed.query)
    if "error" in qs:
        sys.exit(f"LinkedIn recusou a autorização: {qs.get('error_description', qs['error'])}")
    code = qs.get("code", [None])[0]
    if not code:
        sys.exit("Não achei '?code=' na URL colada. Copie a URL inteira da barra de "
                  "endereço, do jeito que o navegador mostrou depois do redirect.")

    resp = requests.post(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=20,
    )
    if resp.status_code != 200:
        sys.exit(f"Falha ao trocar o código por token ({resp.status_code}):\n{resp.text}")
    tok = resp.json()
    access_token = tok["access_token"]
    expires_in = tok.get("expires_in")

    info = requests.get(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=20,
    )
    if info.status_code != 200:
        sys.exit(f"Token obtido, mas falhou ao buscar o perfil ({info.status_code}):\n{info.text}")
    sub = info.json().get("sub")
    if not sub:
        sys.exit(f"Resposta de /v2/userinfo sem 'sub': {info.text}")
    person_urn = f"urn:li:person:{sub}"

    print("Autorização concluída.\n")
    print("Cole estas três variáveis em Environment variables da Routine")
    print("(claude.ai/code/routines → editar → ícone de nuvem → engrenagem do ambiente):\n")
    print(f"LINKEDIN_ACCESS_TOKEN={access_token}")
    print(f"LINKEDIN_PERSON_URN={person_urn}")
    if expires_in:
        import datetime
        expira = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=expires_in)
        print(f"# token expira em ~{expires_in // 86400} dias — por volta de {expira.date()}")
        print("# quando expirar, repita este processo (auth-url, autorizar, exchange)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("auth-url")
    pa.add_argument("--client-id", required=True)
    pa.add_argument("--redirect-uri", default=REDIRECT_URI_PADRAO)

    pe = sub.add_parser("exchange")
    pe.add_argument("--client-id", required=True)
    pe.add_argument("--client-secret", required=True)
    pe.add_argument("--redirect-url", required=True, help="URL completa para onde você foi redirecionado")
    pe.add_argument("--redirect-uri", default=REDIRECT_URI_PADRAO, help="o mesmo cadastrado no app")

    args = p.parse_args()
    if args.cmd == "auth-url":
        auth_url(args.client_id, args.redirect_uri)
    else:
        exchange(args.client_id, args.client_secret, args.redirect_url, args.redirect_uri)


if __name__ == "__main__":
    main()
