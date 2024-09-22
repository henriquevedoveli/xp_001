import logging
from src.model.loader import LoadModel
import numpy as np
from src.database.sqlite import SQliteHandler

class ApiHandler:
    """
    Classe responsável por gerenciar o fluxo de predição de um modelo de machine learning
    e o armazenamento dos resultados no banco de dados.
    """
    
    def __init__(self) -> None:
        """
        Inicializa as instâncias necessárias para o carregamento do modelo e interação com o banco de dados.
        """
        self._model_loader = LoadModel()
        self._sqlite = SQliteHandler()

    @staticmethod
    def _get_prediction(model, features: np.ndarray) -> int:
        """
        Realiza a predição do modelo com base nas features fornecidas.
        
        Parâmetros:
        model: O modelo carregado que será utilizado para a predição.
        features (np.ndarray): Um array de features que servirá de input para o modelo.
        
        Retorno:
        int: O valor da predição realizada pelo modelo.
        
        Exceção:
        Lança um RuntimeError caso ocorra algum erro durante a predição.
        """
        try:
            prediction = model.predict([features])
            return int(prediction[0])
        except Exception as e:
            raise RuntimeError(f"Erro durante a predição do modelo {e}" )

    def predict(self, features) -> int:
        """
        Gerencia o fluxo completo de predição, desde o carregamento do modelo até o armazenamento
        dos resultados no banco de dados.
        
        Parâmetros:
        features: As features que serão utilizadas para realizar a predição.
        
        Retorno:
        int: O valor da predição realizada pelo modelo.
        
        Exceções:
        Lança um RuntimeError caso ocorra algum erro no processo de carregamento do modelo,
        predição ou salvamento dos resultados no banco de dados.
        """
        try:
            logging.info(f"Carregando modelo...")
            model, model_name = self._model_loader.load_model(model_type="mlflow")
            logging.info(f"Modelo carregado com sucesso")

        except Exception as e:
            logging.error("Erro ao carregar modelo {e}", exc_info=True)
            raise RuntimeError("Falha ao carregar o modelo") from e

        try:
            logging.info(f"Iniciando a inferência para o input {features}")
            prediction = self._get_prediction(model, features)
        except RuntimeError as e:
            logging.error("Erro ao realizar a inferência do modelo {e}", exc_info=True)
            raise RuntimeError(f"Erro na predição: {e}")
        
        try:
            logging.info(f"Salvando a inferência do modelo no banco de dados")
            self._sqlite.save_audit_data(model_name=model_name, valores=features, predict=prediction)
            logging.info(f"Dados de inferência salvos com sucesso")
        except Exception as e:
            logging.error("Erro ao salvar a inferência do modelo {e}", exc_info=True)

        return prediction
