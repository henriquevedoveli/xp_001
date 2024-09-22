
# Teste Técnico XP - MLOps
## Henrique Vedoveli

## Visão Geral do Projeto
Este projeto tem como objetivo fornecer uma API para realizar predições utilizando um modelo de Machine Learning. O modelo pode ser carregado localmente (via arquivo `.pkl`) ou através do MLFlow, dependendo da configuração escolhida. A API foi construída utilizando Docker Compose para facilitar a execução e o gerenciamento de dependências.

## Requisitos para Execução

### Dependências:
1. **Modelo de Inferência Local**: 
   - Certifique-se de que o arquivo do modelo (`model.pkl`) esteja presente no diretório `./artifacts/models`.

2. **Modelo via MLFlow**:
   - O serviço MLFlow deve estar em execução na porta `localhost:5000`, e o modelo deve estar treinado e versionado no MLFlow.

3. **Arquivo de Configuração**:
   - O arquivo `parameters.yml` deve estar presente no diretório `./conf` e devidamente configurado.

4. **Porta Disponível**:
   - A porta `9090` deve estar livre para que a API funcione corretamente.

### Executando o Projeto

Para executar o projeto utilizando Docker Compose:

1. Clone o repositório para o seu ambiente local.
2. Na raiz do diretório clonado, execute o seguinte comando:

    ```bash
    sudo docker-compose up -d --build
    ```

    Esse comando fará o build da imagem Docker definida no `Dockerfile` e configurará corretamente o compartilhamento dos volumes necessários.

### Testando a API

A API pode ser testada de duas formas:

1. **Postman**:
   - Utilize a URL `localhost:9090` para fazer as requisições.

   **Rotas Disponíveis**:

   - **GET** `/api/health`:
     - Retorno esperado: 
       ```json
       {"message": "Estou saudável"}
       ```

   - **POST** `/api/predict`:
     - Corpo da requisição (exemplo):
       ```json
       {
         "alcohol": float,
         "malic_acid": float,
         "ash": float,
         "acl": float,
         "mg": int,
         "phenols": float,
         "flavanoids": float,
         "nonflavanoid_phenols": float,
         "proant": float,
         "color": float,
         "hue": float,
         "od": float,
         "proline": int
       }
       ```

     - Retorno esperado:
       ```json
       {"prediction": int}
       ```
2. **SWAGGER**:
    - Utilize a URL `localhost:9090/dpcs` para acessar o SWAGGER.

    - **GET** `/api/health`:
     - Retorno esperado: 
       ```json
       {"message": "Estou saudável"}
       ```

   - **POST** `/api/predict`:
     - Corpo da requisição (exemplo):
       ```json
       {
         "alcohol": float,
         "malic_acid": float,
         "ash": float,
         "acl": float,
         "mg": int,
         "phenols": float,
         "flavanoids": float,
         "nonflavanoid_phenols": float,
         "proant": float,
         "color": float,
         "hue": float,
         "od": float,
         "proline": int
       }
       ```

     - Retorno esperado:
       ```json
       {"prediction": int}
       ```

