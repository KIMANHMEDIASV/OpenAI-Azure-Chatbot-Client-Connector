from typing import Callable, Dict, Any
from ..exceptions import APIError

def get_current_system_status(make_request: Callable) -> Dict[str, Any]:
    """
    Get the current system status.

    Args:
        make_request (Callable): Function to make API requests.

    Returns:
        Dict[str, Any]: The current system status.

    Raises:
        APIError: If the API request fails.
    """
    try:
        return make_request("GET", "/api/System/status/current")
    except APIError as e:
        raise APIError(f"Failed to get current system status: {str(e)}")

def set_current_system_status(make_request: Callable, status: Dict[str, Any]) -> None:
    """
    Set the current system status.

    Args:
        make_request (Callable): Function to make API requests.
        status (Dict[str, Any]): The new system status to set.

    Raises:
        APIError: If the API request fails.
    """
    try:
        make_request("PUT", "/api/System/status/current", json=status)
    except APIError as e:
        raise APIError(f"Failed to set current system status: {str(e)}")