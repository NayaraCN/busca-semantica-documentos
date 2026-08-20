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

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#model = SentenceTransformer(
#    "sentence-transformers/all-MiniLM-L6-v2")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def buscar_semanticamente(documentos, termo, top_k=3):
    textos = [
        documento["texto"]
        for documento in documentos
    ]

    embeddings_documentos = model.encode(textos)

    embedding_consulta = model.encode([termo])

    similaridades = cosine_similarity(
        embedding_consulta,
        embeddings_documentos
    )[0]

    resultados = []

    for documento, score in zip(
        documentos,
        similaridades
    ):
        resultados.append(
            {
                "arquivo": documento["arquivo"],
                "texto": documento["texto"],
                "score": float(score)
            }
        )

    resultados.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return resultados[:top_k]