import yaml
import logging


class Config:
    """
    Classe singleton para carregar e gerenciar a configuração do sistema a partir de um arquivo YAML.
    Garante que apenas uma instância da configuração seja criada e reutilizada ao longo da aplicação.
    """

    _instance = None  # Armazena a única instância da classe
    _config = None  # Armazena as configurações carregadas do arquivo

    def __new__(cls, file_path="/conf/parameters.yml"):
        """
        Cria uma nova instância da classe apenas se não houver uma instância existente.

        Parâmetros:
        file_path (str): O caminho do arquivo de configuração YAML. O valor padrão é "/conf/parameters.yml".

        Retorno:
        Config: Retorna a única instância da classe `Config`.
        """
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._config = cls._load_config(file_path)
        return cls._instance

    @staticmethod
    def _load_config(file_path):
        """
        Carrega o arquivo de configuração YAML do caminho especificado.

        Parâmetros:
        file_path (str): O caminho para o arquivo YAML contendo as configurações.

        Retorno:
        dict: Um dicionário com as configurações carregadas do arquivo YAML.

        Exceções:
        ValueError: Lança uma exceção se o caminho do arquivo estiver incorreto.
        """
        if file_path:
            with open(file_path, "r") as file:
                return yaml.safe_load(
                    file
                )  # Carrega o conteúdo YAML como um dicionário
        else:
            logging.error("O caminho do arquivo config está errado.", exc_info=True)
            raise ValueError("O caminho do arquivo config está errado.")

    def get_config(self):
        """
        Retorna as configurações carregadas.

        Retorno:
        dict: Um dicionário contendo as configurações carregadas do arquivo YAML.
        """
        return self._config
