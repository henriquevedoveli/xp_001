import pickle
import os
from typing import Any

class LoadModel:
    """
    Classe responsavel por carregar um modelo .pkl

    Atributos:
        - model_path: Atributo privado, indica onde esta localizado o modelo a ser carregado

    Metodos:
        - load_model: Carrega e retorna o modelo

    """
    def __init__(self, model_path: str = "/artifacts/models/model.pkl") -> None:
        """
        Iniciliaza a classe.
        
        Parametros:
            - model_path (str): Caminho onde esta localizado o modelo

        Retornos:
            - None

        Raises:
            - FileNotFoundError: Erro ao nao encontrar o arquivo no model_path passado     
        """
        if not os.path.isfile(model_path):
            raise FileNotFoundError(f"O caminho do modelo '{model_path}' não existe.")
        self._model_path = model_path

    def load_model(self) -> Any:
        """
        Carrega o modelo a partir do caminho especificado.
        
        Parametros:
            - None

        Retornos:
            - Any: Modelo Pickler

        Raises:
            - RuntimeError: Erro ao carregar o modelo        
        """
        try:
            with open(self._model_path, 'rb') as model:
                return pickle.load(model)
        except (pickle.PickleError, IOError) as e:
            raise RuntimeError(f"Erro ao carregar o modelo: {e}")
