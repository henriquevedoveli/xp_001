import pickle
import os
import logging
import mlflow.pyfunc
from typing import Any
from src.config.config import Config

class LoadModel:
    """
    Classe responsavel por carregar um modelo .pkl

    Atributos:
        - model_path: Atributo privado, indica onde esta localizado o modelo a ser carregado

    Metodos:
        - load_model: Carrega e retorna o modelo

    """

    def __init__(self) -> None:
        self.config = Config().get_config()

    def load_model(self, model_type:str):

        if model_type == "mlflow":
            logging.info("Usando modelo MLFlow")
            return self.load_mlflow_model()

        elif model_type == "local":
            logging.info("Usando modelo Local")
            return self.load_pickle_model()
        
        logging.error(f"Modo de inferencia {model_type} nao implementado")
        raise ValueError(f"Modo de inferencia {model_type} nao implementado")


        
    def load_mlflow_model(self):

        try:
            model_name = self.config["model"]["mlflow"]["model_name"]
            model_version = self.config["model"]["mlflow"]["model_version"]
            logging.info(f"Carregando modelo MLflow {model_name} versao {model_version}")

            mlflow.set_tracking_uri("http://127.0.0.1:5000")

            return mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}"), model_name
        
        except Exception as e:
            logging.error(f"Erro ao carregar modelo MLFOW {e}")
            return

    def load_pickle_model(self, model_path) -> Any:
        """
        Carrega o modelo a partir do caminho especificado.
        
        Parametros:
            - None

        Retornos:
            - Any: Modelo Pickler

        Raises:
            - RuntimeError: Erro ao carregar o modelo        
        """     
        if not os.path.isfile(model_path):
            logging.error(f"O arquivo {model_path} nao existe")
            raise FileNotFoundError(f"O caminho do modelo '{model_path}' não existe.")
        
        try:
            with open(model_path, 'rb') as model:
                return pickle.load(model), "local"
            logging.info(f"Carregando modelo Local {model_path}")

        except Exception as e:
            logging.error("Erro ao carregar o modelo pickle - {e}", exc_info=True)
            return
