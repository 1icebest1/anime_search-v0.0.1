import os
import json
import requests
import logging
from PySide6.QtCore import QThread, Signal
from bs4 import BeautifulSoup
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

logging.basicConfig(filename='app.log', level=logging.INFO)
DATA_DIR = "data/online"


class AnimeLoaderThread(QThread):
    anime_loaded = Signal(dict)  # Исправлено
    error_occurred = Signal(str)  # Исправлено
    finished = Signal()  # Исправлено

    def __init__(self, parent=None, source_type="video"):
        super().__init__(parent)
        self.source_type = source_type
        self.base_urls = {
            "video": {
                "ru": "https://api.anilibria.tv/v3",
                "en": "https://api.consumet.org",
                "jp": "https://api.allanime.to"
            },
            "text": {
                "ru": "https://shikimori.one/api",
                "en": "https://api.jikan.moe/v4",
                "jp": "https://graphql.anilist.co"
            }
        }

        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    # Остальной код без изменений...

    def run(self):
        try:
            if self.source_type == "video":
                self._load_video_sources()
            else:
                self._load_text_sources()
        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            self.finished.emit()

    def _load_video_sources(self):
        # Приклад для AniLibria
        url = f"{self.base_urls['video']['ru']}/title/updates"
        response = requests.get(url)
        for item in response.json()[:5]:
            self._process_item(item, "video")

    def _load_text_sources(self):
        # Приклад для AniList
        query = gql("""
            query {
                Page(page: 1, perPage: 10) {
                    media(type: ANIME, sort: POPULARITY_DESC) {
                        title { romaji }
                        description
                    }
                }
            }
        """)
        transport = RequestsHTTPTransport(url=self.base_urls['text']['jp'])
        client = Client(transport=transport)
        result = client.execute(query)
        for item in result['Page']['media']:
            self._process_item(item, "text")

    def _process_item(self, data, content_type):
        processed_data = {
            "title": data.get('title', {}).get('romaji', 'Невідомо'),
            "description": data.get('description', ''),
            "type": content_type,
            "source": list(self.base_urls[content_type].keys())[0]
        }
        self._save_to_json(processed_data)
        self.anime_loaded.emit(processed_data)

    def _save_to_json(self, data):
        file_path = os.path.join(DATA_DIR, "data.json")
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logging.error(f"Помилка збереження: {str(e)}")