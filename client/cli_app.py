from requests.exceptions import RequestException

from .api import ImageCaptionClient
from .validators import ImageValidator

class CLIApp:

    def __init__(self, api_client: ImageCaptionClient = None):
        self.api_client = api_client if api_client else ImageCaptionClient()

    def run(self):
        print("=" * 50)
        print("🤖 AI VISION QUERY - TERMINAL INTERFACE 🤖")
        print("=" * 50)
        print("Type 'exit' or 'quit' at any prompt to stop the program.\n")

        while True:
            raw_path = input("\n[?] Enter the path to your image file: ")

            if raw_path.strip().lower() in ["exit", "quit"]:
                break
            cleaned_path = ImageValidator.sanitize_path(raw_path)

            is_valid, message = ImageValidator.validate(cleaned_path)
            if not is_valid:
                print(f"[!] Error: {message}")
                continue

            image_path = message    

            query = input("[?] Enter your question about the image: ").strip()
            if query.lower() in ["exit", "quit"]:
                break

            print("\n[*] Sending data to AI... Please wait...")

            mime_type = ImageValidator.get_mime_type(image_path)

            try:
                result = self.api_client.predict_image(image_path=image_path, query=query, mime_type=mime_type)
                
                print("-" * 40)
                print(f"✅ AI Answer: {result.get('answer', 'No answer found')}")
                print("-" * 40)

            except RequestException as e:
                print(f"[!] Connection/HTTP Error: {e}")
            except Exception as e:
                print(f"[!] Unexpected Error: {e}")

        print("\nGoodbye! See you next time.")
