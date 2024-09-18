from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.api.api_handler import ApiHandler

app = FastAPI()
api_handler = ApiHandler()

class FeaturesInput(BaseModel):
    features: list[float]  

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
        
        preds = api_handler.predict(input_data.features)
        
        return {"prediction": preds}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Erro de validação: {e}")
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {e}")
