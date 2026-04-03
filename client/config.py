import os
from dotenv import load_dotenv

class Settings:
    

    def __init__(self):
        load_dotenv()
        
        self.api_url_raw = os.getenv("API_URL")
        if not self.api_url_raw:
            print("[!] Error: Biến API_URL không được định nghĩa hoặc thiếu file .env!")
            self.base_url = ""
            return

        self.base_url = self.api_url_raw.rstrip("/").removesuffix("/predict")

    @property
    def is_valid(self) -> bool:
        return bool(self.base_url)

settings = Settings()
