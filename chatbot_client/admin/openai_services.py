from typing import Callable, List, Dict, Any
from ..exceptions import APIError, ResourceNotFoundError
from ..models import PagingResult

def get_openai_services(make_request: Callable, search_for: str = None, order_by: str = None, 
                        page_number: int = 1, page_size: int = 20) -> PagingResult:
    """
    Retrieve a list of OpenAI services.

    Args:
        make_request (Callable): Function to make API requests.
        search_for (str, optional): Search term for filtering services.
        order_by (str, optional): Field to order the results by.
        page_number (int, optional): Page number for pagination. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        PagingResult: Paginated result containing OpenAI services.

    Raises:
        APIError: If the API request fails.
    """
    params = {
        "SearchFor": search_for,
        "OrderBy": order_by,
        "PageNumber": page_number,
        "PageSize": page_size
    }
    return make_request("GET", "/api/admin/openAiServices", params=params)

def create_openai_service(make_request: Callable, service_data: Dict[str, Any]) -> str:
    """
    Create a new OpenAI service.

    Args:
        make_request (Callable): Function to make API requests.
        service_data (Dict[str, Any]): Data for the new OpenAI service.

    Returns:
        str: ID of the created OpenAI service.

    Raises:
        APIError: If the API request fails.
    """
    response = make_request("POST", "/api/admin/openAiServices", json=service_data)
    return response

def get_openai_service(make_request: Callable, service_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific OpenAI service.

    Args:
        make_request (Callable): Function to make API requests.
        service_id (str): ID of the OpenAI service to retrieve.

    Returns:
        Dict[str, Any]: Details of the OpenAI service.

    Raises:
        ResourceNotFoundError: If the service is not found.
        APIError: If the API request fails.
    """
    try:
        return make_request("GET", f"/api/admin/openAiServices/{service_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("OpenAI Service", service_id)
        raise

def update_openai_service(make_request: Callable, service_id: str, service_data: Dict[str, Any]) -> None:
    """
    Update an existing OpenAI service.

    Args:
        make_request (Callable): Function to make API requests.
        service_id (str): ID of the OpenAI service to update.
        service_data (Dict[str, Any]): Updated data for the OpenAI service.

    Raises:
        ResourceNotFoundError: If the service is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("PUT", f"/api/admin/openAiServices/{service_id}", json=service_data)
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("OpenAI Service", service_id)
        raise

def delete_openai_service(make_request: Callable, service_id: str) -> None:
    """
    Delete an OpenAI service.

    Args:
        make_request (Callable): Function to make API requests.
        service_id (str): ID of the OpenAI service to delete.

    Raises:
        ResourceNotFoundError: If the service is not found.
        APIError: If the API request fails.
    """
    try:
        make_request("DELETE", f"/api/admin/openAiService/{service_id}")
    except APIError as e:
        if e.status_code == 404:
            raise ResourceNotFoundError("OpenAI Service", service_id)
        raise