from filestack import Client


class FileSharer:

    def __init__(self, file_path, api_key):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        return client.upload(filepath=self.file_path).url