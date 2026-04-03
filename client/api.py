import os
import requests
from requests.exceptions import RequestException
from .config import settings

class ImageCaptionClient:

    def __init__(self, base_url: str = None):
        self.base_url = base_url if base_url is not None else settings.base_url

    def check_root(self) -> dict:
        if not self.base_url: return {"error": "Base URL khong hop le"}
        response = requests.get(f"{self.base_url}/")
        response.raise_for_status()
        return response.json()

    def check_health(self) -> dict:
        if not self.base_url: return {"error": "Base URL khong hop le"}
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

    def predict_image(self, image_path: str, query: str, mime_type: str = "image/jpeg") -> dict:
        if not self.base_url:
            raise ValueError("Chưa cấu hình Base URL hợp lệ.")
            
        with open(image_path, "rb") as image_file:
            files = {"file": (os.path.basename(image_path), image_file, mime_type)}
            data = {"query": query}

            response = requests.post(f"{self.base_url}/predict", files=files, data=data)
            response.raise_for_status()
            
            return response.json()
