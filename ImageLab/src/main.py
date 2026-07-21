# src/main.py
import json
import sys

from .image_pipeline import ImagePipeline


def main():
    prompt = " ".join(sys.argv[1:]) or "Uma paisagem futurista ao pôr do sol"
    result = ImagePipeline().execute_pipeline(prompt, "output_image.jpg")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
