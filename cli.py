from client.config import settings
from client.api import ImageCaptionClient
from client.cli_app import CLIApp

def main():
    if not settings.is_valid:
        return

    api_client = ImageCaptionClient()

    app = CLIApp(api_client=api_client)
    app.run()

if __name__ == "__main__":
    main()