# pages.py - HTML Reader (v1.0)
# by @AghaBanafshi
# همه‌ی HTMLها از پوشه‌ی statics/ خونده می‌شن (با cache، فقط یک بار از دیسک)

from pathlib import Path
from functools import lru_cache

STATICS_DIR = Path(__file__).parent / "statics"


@lru_cache(maxsize=None)
def _read(name: str) -> str:
    """یک فایل HTML رو از statics/ می‌خونه و cache می‌کنه."""
    return (STATICS_DIR / name).read_text(encoding="utf-8")


def get_login_html() -> str:
    return _read("login.html")


def get_dashboard_html() -> str:
    return _read("dashboard.html")


def get_public_page_html(uuid_key: str) -> str:
    """صفحه‌ی پابلیک ساب — UUID رو داخل template جای‌گذاری می‌کنه."""
    return _read("public.html").replace("{uuid_key}", uuid_key)
