from client.config import settings
from client.api import ImageCaptionClient
from requests.exceptions import RequestException
import os

IMAGE_PATH = "test_image.jpg"

def test_root(client: ImageCaptionClient):
    print("\n--- Testing GET / (Root) ---")
    try:
        result = client.check_root()
        print("Kết quả:")
        print(result)
    except Exception as e:
        print("Lỗi khi gọi API root (/):", e)

def test_health(client: ImageCaptionClient):
    print("\n--- Testing GET /health ---")
    try:
        result = client.check_health()
        print("Kết quả:")
        print(result)
    except Exception as e:
        print("Lỗi khi gọi API health (/health):", e)

def test_predict(client: ImageCaptionClient):
    print("\n--- Testing POST /predict ---")
    print(f"Đang gửi ảnh {IMAGE_PATH} lên server...")
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Lỗi: Không tìm thấy ảnh {IMAGE_PATH}")
        return

    try:
        query = "The color of the clothes is "
        result = client.predict_image(image_path=IMAGE_PATH, query=query)
        print("Kết quả:")
        print(result)
    except RequestException as e:
        print("Lỗi HTTP/Kết nối khi gọi API:", e)
    except Exception as e:
        print("Lỗi khi gọi API:", e)

def main():
    if not settings.is_valid:
        return
    
    client = ImageCaptionClient()
    test_root(client)
    test_health(client)
    test_predict(client)

if __name__ == "__main__":
    main()
