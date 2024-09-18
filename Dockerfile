FROM python:3.11

WORKDIR /xp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /artifacts /artifacts

COPY src/ src/

EXPOSE 9090

CMD ["uvicorn", "src.api.server:app", "--host", "0.0.0.0", "--port", "9090"]
