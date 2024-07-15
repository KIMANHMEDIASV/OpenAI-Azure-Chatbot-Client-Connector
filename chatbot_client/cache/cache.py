from typing import Callable
from ..exceptions import APIError

def clear_cache(make_request: Callable) -> None:
    """
    Clear the cache.

    This function sends a request to clear the cache on the server side.

    Args:
        make_request (Callable): Function to make API requests.

    Raises:
        APIError: If the API request fails.

    Returns:
        None
    """
    try:
        make_request("DELETE", "/cache")
    except APIError as e:
        raise APIError(f"Failed to clear cache: {str(e)}")