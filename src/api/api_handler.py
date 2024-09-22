import logging
from src.model.loader import LoadModel
import numpy as np
from src.database.sqlite import SQliteHandler

class ApiHandler:
    def __init__(self) -> None:
        self._model_loader = LoadModel()
        self._sqlite = SQliteHandler()

    @staticmethod
    def _get_prediction(model, features: np.ndarray) -> int:
        try:
            prediction = model.predict([features])

            return int(prediction[0])
        except Exception as e:
            raise RuntimeError(f"Erro durante a predição do modelo {e}" )
        
        

    def predict(self, features) -> int:
        try:
            logging.info(f"Carregando modelo...")
            model, model_name = self._model_loader.load_model(model_type="mlflow")
            logging.info(f"Modelo carregado com sucesso")

        except Exception as e:
            logging.error("Erro ao carregar modelo {e}", exc_info=True)
            raise RuntimeError("Falha ao carregar o modelo") from e

        try:
            logging.info(f"Iniciando a inferencia para o input {features}")
            prediction = self._get_prediction(model, features)
        except RuntimeError as e:
            logging.error("Erro ao realizar a inferencia do modelo {e}", exc_info=True)
            raise RuntimeError(f"Erro na predição: {e}")
        
        try:
            logging.info(f"Salvando a inferencia do modelo no banco de dados")
            self._sqlite.save_audit_data(model_name=model_name, valores=features, predict= prediction)
            logging.info(f"Dados de inferencia salvos com sucessso")
        except Exception as e:
            logging.error("Erro ao realizar salvar a inferencia do modelo {e}", exc_info=True)

        return prediction
