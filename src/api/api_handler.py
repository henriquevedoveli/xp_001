from src.model.loader import LoadModel
import numpy as np

class ApiHandler:
    def __init__(self) -> None:
        self._model_loader = LoadModel()

    @staticmethod
    def _check_features(features, model) -> np.ndarray:
        features = np.array([features])
        
        if features.shape[1] != model.n_features_in_:
            raise ValueError("Incompatibilidade entre as características de entrada e as características do modelo")
        
        return features

    @staticmethod
    def _get_prediction(model, features: np.ndarray) -> int:
        try:
            prediction = model.predict(features)
        except Exception as e:
            raise RuntimeError("Erro durante a predição do modelo") from e
        
        return int(prediction[0])

    def predict(self, features) -> int:
        try:
            model = self._model_loader.load_model()
            print(f"Modelo carregado: {type(model)}")
        except Exception as e:
            raise RuntimeError("Falha ao carregar o modelo") from e

        try:
            features = self._check_features(features, model)
        except ValueError as e:
            raise ValueError(f"Falha na validação das características: {e}")

        try:
            prediction = self._get_prediction(model, features)
        except RuntimeError as e:
            raise RuntimeError(f"Erro na predição: {e}")

        return prediction
