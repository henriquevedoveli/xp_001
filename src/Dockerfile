# Use uma imagem base do Python
FROM python:3.11-bullseye

# Define o diretório de trabalho no container
WORKDIR /src

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Cria a estrutura de diretórios necessária no container
RUN mkdir -p artifacts

COPY ../artifacts artifacts

COPY . .

# Define a variável de ambiente para o uvicorn
ENV UVICORN_CMD="uvicorn src.api.main:app --host 0.0.0.0 --port 8000"

# Exponha a porta na qual o FastAPI irá rodar
EXPOSE 8000

# Define o comando a ser executado quando o container iniciar
CMD ["sh", "-c", "$UVICORN_CMD"]
