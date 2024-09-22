from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.api.api_handler import ApiHandler
import logging

# Inicializa o aplicativo FastAPI e o manipulador de API
app = FastAPI()
api_handler = ApiHandler()

# Configuração de logging para registrar as atividades da API
logging.basicConfig(
    filename="/logs/logs.txt",  # Caminho do arquivo de log
    level=logging.INFO,  # Nível de log: INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato do log
)


class FeaturesInput(BaseModel):
    """
    Modelo de entrada que representa as características necessárias para a predição.
    """

    alcohol: float
    malic_acid: float
    ash: float
    acl: float
    mg: int
    phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proant: float
    color: float
    hue: float
    od: float
    proline: int


@app.get("/api/health")
async def health_check() -> dict:
    """
    Endpoint para verificar a saúde da API.

    Retorno:
    dict: Retorna uma mensagem indicando o status da API.
    """
    return {"message": "Estou saudável"}


@app.post("/api/predict")
async def predict(input_data: FeaturesInput) -> dict:
    """
    Endpoint para obter previsões com base nas características fornecidas.

    Parâmetros:
    input_data (FeaturesInput): Um objeto que contém as características necessárias para a predição.

    Retorno:
    dict: Um dicionário com a predição gerada pelo modelo.

    Exceções:
    HTTPException: Lança exceções HTTP em caso de erro de validação, erro de execução ou erro inesperado.
    """
    try:
        features = [
            input_data.alcohol,
            input_data.malic_acid,
            input_data.ash,
            input_data.acl,
            input_data.mg,
            input_data.phenols,
            input_data.flavanoids,
            input_data.nonflavanoid_phenols,
            input_data.proant,
            input_data.color,
            input_data.hue,
            input_data.od,
            input_data.proline,
        ]

        preds = api_handler.predict(features)

        return {"prediction": preds}

    except ValueError as e:
        logging.error("Erro de validação da requisição {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Erro de validação: {e}")

    except RuntimeError as e:
        logging.error("Erro de execução {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro interno: {e}")

    except Exception as e:
        logging.error("Erro não mapeado {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {e}")
