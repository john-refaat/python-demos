import os

from filestack import Client
from dotenv import load_dotenv

load_dotenv()

class FileUploader:
    def __init__(self):
        self.api_key = os.getenv("FILE_STACK_API_KEY")

    def upload(self, file_path):
        client = Client(self.api_key)
        return client.upload(filepath=file_path).url