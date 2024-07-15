class ChatbotClientError(Exception):
    """Base exception class for ChatbotClient errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class APIError(ChatbotClientError):
    """Exception raised when the API returns an error."""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.status_code = status_code
        self.response = response
        super().__init__(f"API Error: {message}")

class AuthenticationError(ChatbotClientError):
    """Exception raised for authentication errors."""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message)

class RateLimitError(ChatbotClientError):
    """Exception raised when API rate limit is exceeded."""
    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(message)

class InvalidRequestError(ChatbotClientError):
    """Exception raised for invalid requests."""
    def __init__(self, message: str):
        super().__init__(f"Invalid request: {message}")

class ResourceNotFoundError(ChatbotClientError):
    """Exception raised when a requested resource is not found."""
    def __init__(self, resource_type: str, resource_id: str):
        super().__init__(f"{resource_type} with id {resource_id} not found")

class ServerError(ChatbotClientError):
    """Exception raised for server-side errors."""
    def __init__(self, message: str = "Internal server error"):
        super().__init__(message)

class ChatCreationError(ChatbotClientError):
    """Exception raised when chat creation fails."""
    def __init__(self, message: str = "Failed to create chat"):
        super().__init__(message)

class ChatCompletionError(ChatbotClientError):
    """Exception raised when chat completion fails."""
    def __init__(self, message: str = "Failed to get chat completion"):
        super().__init__(message)

class BotOperationError(ChatbotClientError):
    """Exception raised for errors in bot operations."""
    def __init__(self, operation: str, message: str):
        super().__init__(f"Bot {operation} failed: {message}")

class CacheOperationError(ChatbotClientError):
    """Exception raised for errors in cache operations."""
    def __init__(self, operation: str, message: str):
        super().__init__(f"Cache {operation} failed: {message}")

class UserOperationError(ChatbotClientError):
    """Exception raised for errors in user operations."""
    def __init__(self, operation: str, message: str):
        super().__init__(f"User {operation} failed: {message}")

class ConfigurationError(ChatbotClientError):
    """Exception raised for configuration errors."""
    def __init__(self, message: str):
        super().__init__(f"Configuration error: {message}")