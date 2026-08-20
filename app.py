from src.reader import carregar_documentos
from src.search import buscar_palavra


documentos = carregar_documentos("documentos")

termo = input("Digite o termo que deseja pesquisar: ")

resultados = buscar_palavra(
    documentos,
    termo
)


if resultados:

    print("\nArquivos encontrados:\n")

    for resultado in resultados:
        print(
            f"- {resultado['arquivo']}"
        )

else:

    print(
        "\nNenhum documento encontrado."
    )