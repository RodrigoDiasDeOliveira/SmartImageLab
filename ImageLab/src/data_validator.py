# src/data_validator.py
import os

class DataValidator:
    def validate_image(self, image):
        # Verifica se a imagem possui um tamanho válido.
        return (
            image is not None and 
            hasattr(image, 'size') and 
            isinstance(image.size, tuple) and 
            len(image.size) == 2
        )

    def validate_model_path(self, model_path):
        
       # Valida se o caminho fornecido para o modelo é válido.
       # - Deve ser uma string não vazia.
       # - O arquivo/diretório deve existir.
       # - O caminho deve apontar para um arquivo com extensão '.h5', '.pth', ou similar (dependendo do tipo de modelo).
    
        if not isinstance(model_path, str) or not model_path.strip():
            return False  # O caminho deve ser uma string não vazia.

        if not os.path.exists(model_path):
            return False  # O caminho precisa existir no sistema de arquivos.

        # Opcional: verificar extensões permitidas
        valid_extensions = {".h5", ".pth", ".onnx"}  # Extensões típicas de modelos de IA
        if os.path.isfile(model_path):
            _, ext = os.path.splitext(model_path)
            if ext.lower() not in valid_extensions:
                return False  # Extensão do arquivo não é válida.

        return True  # O caminho é válido.

