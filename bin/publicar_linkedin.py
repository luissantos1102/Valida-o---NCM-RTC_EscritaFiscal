#!/usr/bin/env python3
"""Publica o pacote no LinkedIn via API oficial (Posts API, multi-imagem PNG).

Uso:
    python3 bin/publicar_linkedin.py <pacote> [--dry-run]

Lê <pacote>/texto.md e os PNGs em <pacote>/criativo/slide-*.png, sobe cada
imagem, cria o post com todas elas em sequência (o LinkedIn deixa o leitor
folhear entre as imagens, ainda que sem o efeito de página do post de
Documento/PDF) e publica imediatamente.

Por que PNG e não PDF: o post de Documento (PDF) tem visual de "leitura",
como um slide de apresentação. O post multi-imagem é mais rápido de abrir e,
segundo dados que o usuário já checou, engaja melhor. A imagem sai na mesma
resolução gerada por bin/carrossel.py (1080x1350) — nada muda na etapa 5 do
pipeline, só aqui na publicação.

Não há agendamento nativo na API — publicar É agendar, porque quem decide a
hora é a própria Routine, chamando este script no horário certo (17:30).

Variáveis de ambiente exigidas:
    LINKEDIN_ACCESS_TOKEN   obtido via bin/linkedin_oauth.py, dura ~60 dias
    LINKEDIN_PERSON_URN     ex.: urn:li:person:AbCdEfGhIj

Saída: <pacote>/comprovante/resposta_api.json com o retorno da API.
"""
import argparse
import glob
import json
import os
import sys

import requests

API = "https://api.linkedin.com/rest"
LINKEDIN_VERSION = "202601"  # versão da API — ajuste se o LinkedIn recusar por versão vencida


def cabecalhos(token):
    return {
        "Authorization": f"Bearer {token}",
        "LinkedIn-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }


def registrar_upload_imagem(token, person_urn):
    body = {"initializeUploadRequest": {"owner": person_urn}}
    r = requests.post(f"{API}/images?action=initializeUpload",
                       headers=cabecalhos(token), json=body, timeout=20)
    if r.status_code not in (200, 201):
        sys.exit(f"Falha ao iniciar upload de imagem ({r.status_code}):\n{r.text}")
    v = r.json()["value"]
    return v["uploadUrl"], v["image"]


def subir_imagem(upload_url, caminho_png, token):
    with open(caminho_png, "rb") as f:
        r = requests.put(upload_url, data=f.read(),
                          headers={"Authorization": f"Bearer {token}"}, timeout=60)
    if r.status_code not in (200, 201):
        sys.exit(f"Falha ao enviar {caminho_png} ({r.status_code}):\n{r.text}")


def criar_post(token, person_urn, texto, image_urns, dry_run=False):
    body = {
        "author": person_urn,
        "commentary": texto,
        "visibility": "PUBLIC",
        "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []},
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    if len(image_urns) == 1:
        body["content"] = {"media": {"id": image_urns[0]}}
    else:
        body["content"] = {"multiImage": {"images": [{"id": u} for u in image_urns]}}

    if dry_run:
        print("--dry-run: corpo do post que seria enviado a POST /rest/posts:\n")
        print(json.dumps(body, ensure_ascii=False, indent=2))
        return {"dry_run": True, "body": body}

    r = requests.post(f"{API}/posts", headers=cabecalhos(token), json=body, timeout=30)
    if r.status_code not in (200, 201):
        sys.exit(f"Falha ao criar o post ({r.status_code}):\n{r.text}")
    post_urn = r.headers.get("x-restli-id") or r.headers.get("X-RestLi-Id")
    return {"status_code": r.status_code, "post_urn": post_urn, "headers": dict(r.headers)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pacote")
    ap.add_argument("--dry-run", action="store_true",
                     help="monta tudo, mostra o corpo do post, mas NÃO publica")
    args = ap.parse_args()

    token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    person_urn = os.environ.get("LINKEDIN_PERSON_URN")
    if not token or not person_urn:
        sys.exit("Faltam LINKEDIN_ACCESS_TOKEN e/ou LINKEDIN_PERSON_URN no ambiente.\n"
                  "Gere com bin/linkedin_oauth.py e configure na Routine.")

    pkg = os.path.abspath(args.pacote)
    texto_path = os.path.join(pkg, "texto.md")
    if not os.path.exists(texto_path):
        sys.exit(f"{texto_path} não existe.")
    texto = open(texto_path, encoding="utf-8").read().strip()

    slides = sorted(glob.glob(os.path.join(pkg, "criativo", "slide-*.png")))
    if not slides:
        sys.exit(f"Nenhum slide-*.png em {pkg}/criativo — rode bin/carrossel.py antes.")

    print(f"Texto: {len(texto)} caracteres. Slides: {len(slides)}.")

    image_urns = []
    if not args.dry_run:
        for s in slides:
            upload_url, image_urn = registrar_upload_imagem(token, person_urn)
            subir_imagem(upload_url, s, token)
            image_urns.append(image_urn)
            print(f"  enviado: {os.path.basename(s)} → {image_urn}")
    else:
        image_urns = [f"urn:li:image:DRY-RUN-{i}" for i in range(len(slides))]

    resultado = criar_post(token, person_urn, texto, image_urns, dry_run=args.dry_run)

    comprovante_dir = os.path.join(pkg, "comprovante")
    os.makedirs(comprovante_dir, exist_ok=True)
    out = os.path.join(comprovante_dir, "resposta_api.json")
    json.dump(resultado, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    if args.dry_run:
        print(f"\ndry-run salvo em {out}. Nada foi publicado.")
    else:
        urn = resultado.get("post_urn", "")
        print(f"\nPublicado. post_urn={urn}")
        if urn:
            ident = urn.split(":")[-1]
            print(f"Link provável: https://www.linkedin.com/feed/update/{urn}/")
        print(f"Resposta completa em {out}")


if __name__ == "__main__":
    main()
