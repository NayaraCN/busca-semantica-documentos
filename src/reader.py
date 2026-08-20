from pathlib import Path


def carregar_documentos(pasta: str):
    documentos = []

    caminho_pasta = Path(pasta)

    for arquivo in caminho_pasta.glob("*.txt"):
        texto = arquivo.read_text(
            encoding="utf-8"
        )

        documentos.append(
            {
                "arquivo": arquivo.name,
                "texto": texto
            }
        )

    return documentos