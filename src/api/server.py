from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.api.api_handler import ApiHandler
import logging

app = FastAPI()
api_handler = ApiHandler()

logging.basicConfig(
    filename='/logs/logs.txt',  
    level=logging.INFO,        
    format='%(asctime)s - %(levelname)s - %(message)s', 
)

class FeaturesInput(BaseModel):
    alcohol:float
    malic_acid:float
    ash: float
    acl: float
    mg:int
    phenols:float
    flavanoids:float
    nonflavanoid_phenols:float
    proant:float
    color:float
    hue:float
    od:float
    proline:int

@app.get("/api/health")
async def health_check() -> dict:
    """
    Endpoint para verificar a saúde da API.
    """
    return {"message": "Estou saudável"}

@app.post("/api/predict")
async def predict(input_data: FeaturesInput) -> dict:
    """
    Endpoint para obter previsões com base nas características fornecidas.
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
            input_data.proline
        ]
        
        preds = api_handler.predict(features)
        
        return {"prediction": preds}
    
    except ValueError as e:
        logging.error("Erro de validacao da requisicao {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Erro de validação: {e}")
    except RuntimeError as e:
        logging.error("Erro de execuacao {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro interno: {e}")
    except Exception as e:
        logging.error("Erro nao mapeadp {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {e}")
