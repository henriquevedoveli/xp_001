import pickle
import os
import logging
import mlflow.pyfunc
from typing import Any
from src.config.config import Config


class LoadModel:
    """
    Classe responsável por carregar modelos para inferência, seja de um serviço MLflow ou de um arquivo local em formato pickle.
    """

    def __init__(self) -> None:
        """
        Inicializa a classe carregando as configurações do arquivo de configuração.
        """
        self.config = Config().get_config()  # Carrega as configurações do sistema

    def load_model(self, model_type: str):
        """
        Carrega o modelo com base no tipo de inferência especificado.

        Parâmetros:
        model_type (str): Tipo de modelo a ser carregado ("mlflow" ou "local").

        Retorno:
        tuple: O modelo carregado e o nome do modelo.

        Exceções:
        ValueError: Lança uma exceção se o tipo de inferência não for implementado.
        """
        if model_type == "mlflow":
            logging.info("Usando modelo MLFlow")
            return self.load_mlflow_model()

        elif model_type == "local":
            logging.info("Usando modelo Local")
            return self.load_pickle_model()

        logging.error(f"Modo de inferência {model_type} não implementado")
        raise ValueError(f"Modo de inferência {model_type} não implementado")

    def load_mlflow_model(self):
        """
        Carrega o modelo de inferência a partir do MLflow.

        Retorno:
        tuple: O modelo carregado e o nome do modelo.

        Exceções:
        Exception: Lança uma exceção em caso de erro ao carregar o modelo via MLflow.
        """
        try:
            model_name = self.config["model"]["mlflow"]["model_name"]
            model_version = self.config["model"]["mlflow"]["model_version"]
            logging.info(
                f"Carregando modelo MLflow {model_name} versão {model_version}"
            )

            mlflow.set_tracking_uri(
                "http://127.0.0.1:5000"
            )  # Define a URI do servidor MLflow

            return (
                mlflow.pyfunc.load_model(
                    model_uri=f"models:/{model_name}/{model_version}"
                ),
                model_name,
            )

        except Exception as e:
            logging.error(f"Erro ao carregar modelo MLflow {e}")
            return

    def load_pickle_model(self, model_path: str) -> Any:
        """
        Carrega o modelo de inferência de um arquivo pickle local.

        Parâmetros:
        model_path (str): O caminho do arquivo pickle.

        Retorno:
        tuple: O modelo carregado e o nome do modelo ("local").

        Exceções:
        FileNotFoundError: Lança uma exceção se o caminho do arquivo não for encontrado.
        Exception: Lança uma exceção em caso de erro ao carregar o modelo pickle.
        """
        if not os.path.isfile(model_path):
            logging.error(f"O arquivo {model_path} não existe")
            raise FileNotFoundError(f"O caminho do modelo '{model_path}' não existe.")

        try:
            with open(model_path, "rb") as model:
                logging.info(f"Carregando modelo Local {model_path}")
                return pickle.load(model), "local"

        except Exception as e:
            logging.error(f"Erro ao carregar o modelo pickle - {e}", exc_info=True)
            return
