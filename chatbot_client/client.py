import requests
from typing import Optional
from .exceptions import ChatbotClientError
from .cache.cache import clear_cache
from .admin import openai_services, bots
from .bot import bot
from .statistic import statistic
from .system import system
from .user import user
from .chat import chat as chat_module  # Ensure consistent import

class ChatbotClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def _make_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ChatbotClientError(f"API request failed: {str(e)}")

    # Chat operations
    def create_chat(self, bot_id: str) -> str:
        return chat_module.create_chat(self._make_request, bot_id)

    def chat_completion(self, chat_id: str, user_message: str) -> str:
        return chat_module.chat_completion(self._make_request, chat_id, user_message)

    def delete_chat(self, chat_id: str) -> None:
        return chat_module.delete_chat(self._make_request, chat_id)

    # Bot operations
    def search_bot(self, bot_id: str, query: str) -> dict:
        return bot.search_bot(self._make_request, bot_id, query)

    def get_bots(self) -> list:
        return bot.get_bots(self._make_request)

    # Admin operations
    def get_openai_services(self) -> list:
        return openai_services.get_openai_services(self._make_request)

    def create_bot(self, bot_data: dict) -> str:
        return bots.create_bot(self._make_request, bot_data)

    def clear_cache(self):
        return clear_cache(self._make_request)

    # Statistic operations
    def get_token_usage(self, **params) -> dict:
        return statistic.get_token_usage(self._make_request, **params)

    # System operations
    def get_system_status(self) -> dict:
        return system.get_system_status(self._make_request)

    # User operations
    def get_current_user(self) -> dict:
        return user.get_current_user(self._make_request)

    def update_user_settings(self, settings: dict) -> None:
        return user.update_user_settings(self._make_request)

    # Add more methods here as needed for other operations
