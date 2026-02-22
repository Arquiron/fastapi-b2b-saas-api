import hashlib
import secrets
from app.core.config import settings

def hash_api_key(api_key: str) -> str:
    raw = (settings.api_key_pepper + api_key).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def safe_equals(a: str, b: str) -> bool:
    return secrets.compare_digest(a, b)