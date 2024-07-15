from typing import Callable, Dict, Any, List
from ..exceptions import APIError, ResourceNotFoundError
from ..models import PagingResult

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
    return make_request("GET", "/api/admin/bots", params=params)

def create_bot(make_request: Callable, bot_data: Dict[str, Any]) -> str:
    """
    Create a new bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_data (Dict[str, Any]): Data for the new bot.

    Returns:
        str: ID of the created bot.

    Raises:
        APIError: If the API request fails.
    """
    response = make_request("POST", "/api/admin/bots", json=bot_data)
    return response["botId"]

def get_bot(make_request: Callable, bot_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to retrieve.

    Returns:
        Dict[str, Any]: Details of the bot.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    try:
        return make_request("GET", f"/api/admin/bots/{bot_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

def update_bot(make_request: Callable, bot_id: str, bot_data: Dict[str, Any]) -> None:
    """
    Update an existing bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to update.
        bot_data (Dict[str, Any]): Updated data for the bot.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("PUT", f"/api/admin/bots/{bot_id}", json=bot_data)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

def delete_bot(make_request: Callable, bot_id: str) -> None:
    """
    Delete a bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to delete.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("DELETE", f"/api/admin/bots/{bot_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

def get_bot_facts(make_request: Callable, bot_id: str, search_for: str = None, order_by: str = None, 
                  page_number: int = 1, page_size: int = 20) -> PagingResult:
    """
    Retrieve facts for a specific bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to retrieve facts for.
        search_for (str, optional): Search term for filtering facts.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        PagingResult: Paginated result containing bot facts.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    try:
        return make_request("GET", f"/api/admin/bots/{bot_id}/facts", params=params)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

def create_bot_fact(make_request: Callable, bot_id: str, fact_data: Dict[str, Any]) -> str:
    """
    Create a new fact for a bot.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str): ID of the bot to create a fact for.
        fact_data (Dict[str, Any]): Data for the new fact.

    Returns:
        str: ID of the created fact.

    Raises:
        ResourceNotFoundError: If the bot is not found.
        APIError: If the API request fails.
    """
    try:
        response = make_request("POST", f"/api/admin/bots/{bot_id}/facts", json=fact_data)
        return response["botFactId"]
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("Bot", bot_id)
        raise

# Additional functions for other bot-related operations can be added here