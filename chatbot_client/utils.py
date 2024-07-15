import json
from typing import Any, Dict, Optional
from datetime import datetime, date
from .exceptions import ConfigurationError

def json_serial(obj: Any) -> str:
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def to_camel_case(snake_str: str) -> str:
    """Convert snake_case string to camelCase"""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_snake_case(camel_str: str) -> str:
    """Convert camelCase string to snake_case"""
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_str]).lstrip('_')

def camel_case_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively convert dictionary keys from snake_case to camelCase"""
    if not isinstance(d, dict):
        return d
    return {to_camel_case(k): camel_case_dict(v) for k, v in d.items()}

def snake_case_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively convert dictionary keys from camelCase to snake_case"""
    if not isinstance(d, dict):
        return d
    return {to_snake_case(k): snake_case_dict(v) for k, v in d.items()}

def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file"""
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        raise ConfigurationError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError:
        raise ConfigurationError(f"Invalid JSON in configuration file: {config_path}")

def validate_api_key(api_key: Optional[str]) -> None:
    """Validate the API key"""
    if not api_key:
        raise ConfigurationError("API key is required")
    if not isinstance(api_key, str):
        raise ConfigurationError("API key must be a string")
    if len(api_key) < 32:  # Assuming a minimum length for API keys
        raise ConfigurationError("API key seems too short")

def truncate_string(s: str, max_length: int) -> str:
    """Truncate a string to a maximum length, adding ellipsis if truncated"""
    return (s[:max_length-3] + '...') if len(s) > max_length else s

def format_error_message(error: Exception) -> str:
    """Format an exception into a readable error message"""
    return f"{type(error).__name__}: {str(error)}"

def parse_datetime(dt_string: str) -> datetime:
    """Parse a datetime string into a datetime object"""
    try:
        return datetime.fromisoformat(dt_string.replace('Z', '+00:00'))
    except ValueError:
        raise ValueError(f"Invalid datetime format: {dt_string}")

def generate_user_agent() -> str:
    """Generate a user agent string for the client"""
    from . import __version__  # Assuming you have a __version__ in your __init__.py
    return f"ChatbotClient/{__version__} Python"