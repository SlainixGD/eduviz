# eduviz/media.py
class MediaHandler:
    def __init__(self):
        self.media_files = []

    def add_media(self, file_path):
        self.media_files.append(file_path)
        print(f"Added media file: {file_path}")

    def play_media(self):
        for file in self.media_files:
            print(f"Playing media file: {file}")