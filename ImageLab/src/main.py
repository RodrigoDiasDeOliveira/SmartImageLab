# src/main.py
from image_pipeline import ImagePipeline

def main():
    pipeline = ImagePipeline()
    prompt = "Uma descrição para gerar a imagem"
    image_name = "output_image.jpg"
    result = pipeline.execute_pipeline(prompt, image_name)
    print(result)

if __name__ == "__main__":
    main()
