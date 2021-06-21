# Projeto API Rick and Morty

## Instalação
O projeto usa uma instância de banco de dados Mongo e algumas bibliotecas do Python, como `flask`, `requests` e `pymongo`. A versão do Python usada é a `3.9.5`.

### MongoDB
Existem três alternativas para usar o MongoDB:

1. Baixando e instalando em sua máquina: [site oficial do Mongo](https://www.mongodb.com/)
1. Criando uma instância gratuita no Atlas: [Mongo Atlas](https://www.mongodb.com/cloud/atlas)
1. Utilizando uma imagem pronta do docker: [link para o Docker Hub](https://hub.docker.com/_/mongo)

### Bibliotecas Python
Todas as dependências do projeto se encontram no arquivo [requirements.txt](requirements.txt). Para instalá-las, basta executar

    pip install -r requirements.txt

no PowerShell do Windows ou terminal do Unix (Linux/MacOS). Adicionalmente, você pode querer executar este comando de dentro de um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html).

## Configuração
O projeto possui uma configuração simples que consiste de opcionalmente definir duas variáveis de ambiente: `MONGO_DBNAME` e `MONGO_CONN_URL`, como pode ser visto no arquivo [config.py](config.py).

A variável de ambiente `MONGO_CONN_URL` só é necessária caso você use a instância do Atlas. Caso instale localmente ou use docker (com as devidas portas expostas), ela não deve ser necessária.

## Execução
    python app.py

O comando acima sobe um servidor Flask na porta 5000 que pode ser acessado pelo [http://localhost:5000](http://localhost:5000).
