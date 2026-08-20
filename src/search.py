def buscar_palavra(documentos, termo):
    resultados = []

    termo = termo.lower()

    for documento in documentos:

        texto = documento["texto"].lower()

        if termo in texto:

            resultados.append(
                {
                    "arquivo": documento["arquivo"],
                    "texto": documento["texto"]
                }
            )

    return resultados