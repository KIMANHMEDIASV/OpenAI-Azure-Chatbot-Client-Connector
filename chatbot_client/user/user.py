from typing import Callable, Dict, Any, List, Optional
from ..exceptions import APIError, ResourceNotFoundError

def get_current_user(make_request: Callable) -> Dict[str, Any]:
    """Get the current user's information."""
    return make_request("GET", "/api/users/current")

def update_current_user(make_request: Callable, user_data: Dict[str, Any]) -> None:
    """Update the current user's information."""
    make_request("PUT", "/api/users/current", json=user_data)

def accept_terms(make_request: Callable) -> None:
    """Accept the terms for the current user."""
    make_request("PUT", "/api/users/current/acceptTerms")

def delete_current_user_chats(make_request: Callable, keep_favorites: bool) -> None:
    """Delete all chats for the current user."""
    make_request("DELETE", f"/api/users/current/chats/all/{str(keep_favorites).lower()}")

def delete_current_user_chat_by_id(make_request: Callable, chat_id: str) -> None:
    """Delete a specific chat for the current user."""
    make_request("DELETE", f"/api/users/current/chats/byid/{chat_id}")

def delete_current_user_chat_completion_by_id(make_request: Callable, chat_id: str, completion_id: str) -> None:
    """Delete a specific chat completion for the current user."""
    make_request("DELETE", f"/api/users/current/chats/{chat_id}/completion/{completion_id}")

def delete_current_user_chats_by_bot_id(make_request: Callable, bot_id: str, keep_favorites: bool) -> None:
    """Delete all chats for a specific bot for the current user."""
    make_request("DELETE", f"/api/users/current/chats/bybot/{bot_id}/{str(keep_favorites).lower()}")

def delete_current_user_chats_by_bot_id_and_system_message_id(make_request: Callable, bot_id: str, system_message_id: str, keep_favorites: bool) -> None:
    """Delete all chats for a specific bot and system message for the current user."""
    make_request("DELETE", f"/api/users/current/chats/bybot/{bot_id}/{system_message_id}/{str(keep_favorites).lower()}")

def get_current_user_chats_by_bot(make_request: Callable, bot_id: str, only_favorites: bool = False, search_for: Optional[str] = None, order_by: Optional[str] = None, page_number: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """Get chats for a specific bot for the current user."""
    params = {
        "OnlyFavorites": only_favorites,
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", f"/api/users/current/chats/{bot_id}", params=params)

def get_current_user_chats_by_bot_and_systemprompt(make_request: Callable, bot_id: str, user_systemprompt_id: str, only_favorites: bool = False, search_for: Optional[str] = None, order_by: Optional[str] = None, page_number: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """Get chats for a specific bot and system prompt for the current user."""
    params = {
        "OnlyFavorites": only_favorites,
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", f"/api/users/current/chats/{bot_id}/{user_systemprompt_id}", params=params)

def get_current_user_chats(make_request: Callable, only_favorites: bool = False, search_for: Optional[str] = None, order_by: Optional[str] = None, page_number: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """Get all chats for the current user."""
    params = {
        "OnlyFavorites": only_favorites,
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", "/api/users/current/chats", params=params)

def update_chat_is_favorite(make_request: Callable, chat_id: str, is_favorite: bool) -> None:
    """Update whether a chat is marked as favorite for the current user."""
    make_request("PUT", f"/api/users/current/chats/{chat_id}/isfavorite", json={"isFavorite": is_favorite})

def get_user_system_messages(make_request: Callable, search_for: Optional[str] = None, order_by: Optional[str] = None, page_number: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """Get system messages for the current user."""
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", "/api/users/current/userSystemMessage", params=params)

def create_user_system_message(make_request: Callable, message_data: Dict[str, Any]) -> str:
    """Create a new system message for the current user."""
    response = make_request("POST", "/api/users/current/userSystemMessage", json=message_data)
    return response

def get_user_system_message(make_request: Callable, message_id: str) -> Dict[str, Any]:
    """Get a specific system message for the current user."""
    return make_request("GET", f"/api/users/current/userSystemMessage/{message_id}")

def update_user_system_message(make_request: Callable, message_id: str, message_data: Dict[str, Any]) -> None:
    """Update a specific system message for the current user."""
    make_request("PUT", f"/api/users/current/userSystemMessage/{message_id}", json=message_data)

def delete_user_system_message(make_request: Callable, message_id: str) -> None:
    """Delete a specific system message for the current user."""
    make_request("DELETE", f"/api/users/current/userSystemMessage/{message_id}")

def get_user_system_message_count(make_request: Callable) -> Dict[str, int]:
    """Get the count of system messages for the current user."""
    return make_request("GET", "/api/users/current/userSystemMessageCount")