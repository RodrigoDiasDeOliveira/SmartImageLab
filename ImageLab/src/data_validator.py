# src/data_validator.py
class DataValidator:
    def validate_image(self, image):
        return image is not None and hasattr(image, 'size')

    def validate_model_path(self, model_path):
        # Implementação de validação do caminho do modelo.
