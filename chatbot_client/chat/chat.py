from typing import Callable, Dict, Any
from ..exceptions import APIError, ResourceNotFoundError

def create_chat(make_request: Callable, bot_id: str) -> Dict[str, Any]:
    """
    Create a new chat session.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to chat with.

    Returns:
        Dict[str, Any]: Details of the created chat session.

    Raises:
        APIError: If the API request fails.
    """
    data = {"botId": bot_id}
    return make_request("POST", "/api/chats", json=data)

def create_chat_by_bot_code(make_request: Callable, bot_code: str) -> Dict[str, Any]:
    """
    Create a new chat session using a bot code.

    Args:
        make_request (Callable): Function to make API requests.
        bot_code (str): Code of the bot to chat with.

    Returns:
        Dict[str, Any]: Details of the created chat session.

    Raises:
        APIError: If the API request fails.
    """
    data = {"botCode": bot_code}
    return make_request("POST", "/api/chats/create/bybotcode", json=data)

def chat_completion(make_request: Callable, chat_id: str, user_message: str, ignore_chat_history: bool = False, is_admin_chat: bool = False, is_trace_log_enabled: bool = False) -> Dict[str, Any]:
    """
    Send a message to the chatbot and get a response.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.
        user_message (str): Message to send to the chatbot.
        ignore_chat_history (bool): Whether to ignore chat history.
        is_admin_chat (bool): Whether this is an admin chat.
        is_trace_log_enabled (bool): Whether to enable trace logging.

    Returns:
        Dict[str, Any]: Chatbot's response and other details.

    Raises:
        APIError: If the API request fails.
    """
    data = {
        "userMessage": user_message,
        "ignoreChatHistory": ignore_chat_history,
        "isAdminChat": is_admin_chat,
        "isTraceLogEnabled": is_trace_log_enabled
    }
    return make_request("POST", f"/api/chats/{chat_id}/completions", json=data)

def get_chat(make_request: Callable, chat_id: str) -> Dict[str, Any]:
    """
    Get details of a specific chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.

    Returns:
        Dict[str, Any]: Details of the chat session.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    try:
        return make_request("GET", f"/api/chats/{chat_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def delete_chat(make_request: Callable, chat_id: str) -> None:
    """
    Delete a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session to delete.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("DELETE", f"/api/chats/{chat_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def bot_feedback(make_request: Callable, chat_id: str, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Submit feedback for a bot.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.
        feedback_data (Dict[str, Any]): Feedback data to submit.

    Returns:
        Dict[str, Any]: Response containing the feedback ID.

    Raises:
        APIError: If the API request fails.
    """
    return make_request("POST", f"/api/chats/{chat_id}/feedback", json=feedback_data)

def get_open_chat_bot_id(make_request: Callable) -> Dict[str, Any]:
    """
    Get the ID of the open chat bot.

    Args:
        make_request (Callable): Function to make API requests.

    Returns:
        Dict[str, Any]: Details of the open chat bot.

    Raises:
        APIError: If the API request fails.
    """
    return make_request("GET", "/api/chats/OpenChatBotId")

def update_chat_display_name(make_request: Callable, chat_id: str, display_name: str) -> None:
    """
    Update the display name of a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.
        display_name (str): New display name for the chat.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    data = {"displayName": display_name}
    try:
        make_request("PUT", f"/api/chats/{chat_id}/displayName", json=data)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def update_chat_user_system_message(make_request: Callable, chat_id: str, user_system_message_id: str) -> None:
    """
    Update the user system message for a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.
        user_system_message_id (str): ID of the user system message.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    data = {"userSystemMessageId": user_system_message_id}
    try:
        make_request("PUT", f"/api/chats/{chat_id}/userSystemMessage", json=data)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def delete_chat_user_system_message(make_request: Callable, chat_id: str) -> None:
    """
    Delete the user system message for a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("DELETE", f"/api/chats/{chat_id}/userSystemMessage")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def create_chat_one_time_ticket(make_request: Callable, chat_id: str) -> str:
    """
    Create a one-time ticket for a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.

    Returns:
        str: The created one-time ticket.

    Raises:
        ResourceNotFoundError: If the chat is not found.
        APIError: If the API request fails.
    """
    try:
        return make_request("POST", f"/api/chats/{chat_id}/tickets")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat", chat_id)
        raise

def get_chat_download(make_request: Callable, chat_id: str, path: str, ticket: str) -> bytes:
    """
    Get a download from a chat session.

    Args:
        make_request (Callable): Function to make API requests.
        chat_id (str): ID of the chat session.
        path (str): Path of the download.
        ticket (str): One-time ticket for the download.

    Returns:
        bytes: The downloaded content.

    Raises:
        ResourceNotFoundError: If the chat or download is not found.
        APIError: If the API request fails.
    """
    params = {"ticket": ticket}
    try:
        return make_request("GET", f"/api/chats/{chat_id}/downloads/{path}", params=params, return_raw=True)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Chat or Download", f"{chat_id}/{path}")
        raise