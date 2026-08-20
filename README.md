# Busca Semantica de Documentos

Aplicacao em Python para pesquisar documentos de texto a partir de um termo informado pelo usuario. O projeto oferece duas modalidades:

- **Busca exata:** localiza os arquivos que contem o termo pesquisado, sem diferenciar letras maiusculas e minusculas.
- **Busca semantica:** compara o significado do termo com o conteudo dos documentos usando embeddings e retorna os tres arquivos mais similares, acompanhados do score de similaridade.

## Finalidade

Facilitar a localizacao de informacoes em um conjunto de documentos `.txt`, permitindo tanto uma consulta direta por palavra quanto uma consulta baseada em semelhanca de significado. A busca semantica e especialmente util quando o termo pesquisado nao aparece literalmente no documento, mas o assunto esta relacionado.

## Requisitos

- Python 3.10 ou superior
- `pip`
- Acesso a internet na primeira execucao da busca semantica, para baixar o modelo da biblioteca `sentence-transformers`

## Instalacao

1. Clone o repositorio ou abra a pasta do projeto:

	```bash
	cd busca-semantica-documentos
	```

2. Crie um ambiente virtual:

	```bash
	python -m venv .venv
	```

3. Ative o ambiente virtual.

	No Windows PowerShell:

	```powershell
	.\.venv\Scripts\Activate.ps1
	```

	No Windows Prompt de Comando:

	```bat
	.venv\Scripts\activate.bat
	```

4. Instale as dependencias:

	```bash
	pip install -r requirements.txt
	```

## Execucao

Com o ambiente virtual ativado, execute:

```bash
python app.py
```

Depois:

1. Escolha `1` para busca exata ou `2` para busca semantica.
2. Informe o termo que deseja pesquisar.
3. Consulte os arquivos encontrados no terminal.

Na busca semantica, o modelo pode ser baixado automaticamente na primeira execucao. As execucoes seguintes normalmente aproveitam o modelo armazenado em cache.

## Estrutura do projeto

```text
.
├── app.py                  # Interface de linha de comando
├── requirements.txt        # Dependencias do projeto
├── documentos/             # Documentos .txt pesquisados
└── src/
	 ├── reader.py           # Carregamento dos documentos
	 └── search.py           # Busca exata e busca semantica
```

## Adicionando documentos

Coloque novos arquivos com extensao `.txt` diretamente na pasta `documentos/`. Eles serao carregados automaticamente quando o programa for iniciado.

Os arquivos devem estar codificados em UTF-8.

## Observacoes

- A busca exata retorna somente os nomes dos arquivos que contem o termo.
- A busca semantica retorna ate tres resultados ordenados do maior para o menor score.
- O modelo utilizado e `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, adequado para consultas em portugues e outros idiomas.
