from typing import Callable, Dict, Any, Optional
from datetime import date
from ..exceptions import APIError

def update_statistic(make_request: Callable) -> None:
    """
    Update the statistics.

    Args:
        make_request (Callable): Function to make API requests.

    Raises:
        APIError: If the API request fails.
    """
    try:
        make_request("PUT", "/api/statistic")
    except APIError as e:
        raise APIError(f"Failed to update statistics: {str(e)}")

def get_token_usage_statistic(
    make_request: Callable,
    bot_id: Optional[str] = None,
    token_usage_type_id: Optional[int] = None,
    from_request_date: Optional[date] = None,
    to_request_date: Optional[date] = None,
    search_for: Optional[str] = None,
    order_by: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 20
) -> Dict[str, Any]:
    """
    Get token usage statistics.

    Args:
        make_request (Callable): Function to make API requests.
        bot_id (str, optional): ID of the bot to get statistics for.
        token_usage_type_id (int, optional): Type of token usage.
        from_request_date (date, optional): Start date for the statistics.
        to_request_date (date, optional): End date for the statistics.
        search_for (str, optional): Search term for filtering statistics.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        Dict[str, Any]: Token usage statistics.

    Raises:
        APIError: If the API request fails.
    """
    params = {
        "BotId": bot_id,
        "TokenUsageTypeId": token_usage_type_id,
        "FromRequestDate": from_request_date.isoformat() if from_request_date else None,
        "ToRequestDate": to_request_date.isoformat() if to_request_date else None,
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    try:
        return make_request("GET", "/api/statistic/tokenUsageStatistic", params=params)
    except APIError as e:
        raise APIError(f"Failed to get token usage statistics: {str(e)}")