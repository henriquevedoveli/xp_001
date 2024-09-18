FROM python:3.11-bullseye

WORKDIR /xp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p artifacts

COPY ../artifacts artifacts

COPY src/ src/

# Define a variável de ambiente para o uvicorn
ENV UVICORN_CMD="uvicorn src.api.server:app --host 0.0.0.0 --port 9090"

# Exponha a porta na qual o FastAPI irá rodar
EXPOSE 9090

# Define o comando a ser executado quando o container iniciar
CMD ["sh", "-c", "$UVICORN_CMD"]
