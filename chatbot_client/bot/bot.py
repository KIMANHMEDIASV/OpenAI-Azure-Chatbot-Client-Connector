from typing import Callable, Dict, Any, List
from ..exceptions import APIError, ResourceNotFoundError
from ..models import PagingResult

def search_bot(make_request: Callable, bot_id: str, query: str) -> str:
    """
    Search for a bot using a query.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to search.
        query (str): Search query.

    Returns:
        str: Search result.

    Raises:
        APIError: If the API request fails.
    """
    data = {"userMessage": query}
    return make_request("POST", f"/api/bots/{bot_id}/search", json=data)

def get_bots(make_request: Callable, search_for: str = None, order_by: str = None, 
             page_number: int = 1, page_size: int = 20) -> PagingResult:
    """
    Retrieve a list of bots.

    Args:
        make_request (Callable): Function to make API requests.
        search_for (str, optional): Search term for filtering bots.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        PagingResult: Paginated result containing bots.

    Raises:
        APIError: If the API request fails.
    """
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", "/api/bots", params=params)

def get_bots_by_start_bot(make_request: Callable, start_bot_id: str, search_for: str = None, 
                          order_by: str = None, page_number: int = 1, page_size: int = 20) -> PagingResult:
    """
    Retrieve a list of bots associated with a start bot.

    Args:
        make_request (Callable): Function to make API requests.
        start_bot_id (str): ID of the start bot.
        search_for (str, optional): Search term for filtering bots.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        PagingResult: Paginated result containing bots.

    Raises:
        APIError: If the API request fails.
    """
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", f"/api/bots/bystartbot/{start_bot_id}", params=params)

def get_start_bots(make_request: Callable, search_for: str = None, order_by: str = None, 
                   page_number: int = 1, page_size: int = 20) -> PagingResult:
    """
    Retrieve a list of start bots.

    Args:
        make_request (Callable): Function to make API requests.
        search_for (str, optional): Search term for filtering start bots.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        PagingResult: Paginated result containing start bots.

    Raises:
        APIError: If the API request fails.
    """
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", "/api/bots/startbots", params=params)

def get_bot_image(make_request: Callable, bot_id: str) -> bytes:
    """
    Retrieve the image for a specific bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot.

    Returns:
        bytes: Bot image data.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    try:
        return make_request("GET", f"/api/bots/botimage/{bot_id}", return_raw=True)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

def is_stop_all_bots(make_request: Callable) -> bool:
    """
    Check if all bots are stopped.

    Args:
        make_request (Callable): Function to make API requests.

    Returns:
        bool: True if all bots are stopped, False otherwise.

    Raises:
        APIError: If the API request fails.
    """
    return make_request("GET", "/api/bots/stop")