from src.reader import carregar_documentos
from src.search import buscar_palavra, buscar_semanticamente


documentos = carregar_documentos("documentos")

print("Escolha o tipo de busca:")
print("1 - Busca exata")
print("2 - Busca semântica")

tipo_busca = input("\nOpção: ")

termo = input(
    "\nDigite o termo que deseja pesquisar: "
)


if tipo_busca == "1":

    resultados = buscar_palavra(
        documentos,
        termo
    )

    if resultados:

        print("\nArquivos encontrados:\n")

        for resultado in resultados:
            print(f"- {resultado['arquivo']}")

    else:

        print("\nNenhum documento encontrado.")


elif tipo_busca == "2":

    resultados = buscar_semanticamente(
        documentos,
        termo
    )

    print("\nResultados semânticos:\n")

    for resultado in resultados:

        print(
            f"Arquivo: {resultado['arquivo']}"
        )

        print(
            f"Similaridade: {resultado['score']:.2f}"
        )

        print("-" * 50)

else:

    print("Opção inválida.")