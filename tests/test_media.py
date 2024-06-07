# tests/test_media.py
import unittest
from eduviz.media import MediaHandler

class TestMediaHandler(unittest.TestCase):
    def test_add_and_play_media(self):
        media_handler = MediaHandler()
        media_handler.add_media("test_media.mp4")
        self.assertIn("test_media.mp4", media_handler.media_files)

if __name__ == '__main__':
    unittest.main()