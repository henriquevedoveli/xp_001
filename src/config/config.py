import yaml
import logging

class Config:
    _instance = None
    _config = None

    def __new__(cls, file_path="/conf/parameters.yml"):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._config = cls._load_config(file_path)
        return cls._instance

    @staticmethod
    def _load_config(file_path):
        if file_path:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        else:
            logging.error("O caminho do arquivo config esta errado.", exc_info=True)
            raise ValueError("O caminho do arquivo config esta errado.")

    def get_config(self):
        return self._config