import os
import pytest
from dotenv import load_dotenv
from api_client import YougileProjects

load_dotenv()


@pytest.fixture
def api():
    base_url = "https://ru.yougile.com"
    # Для наставника: токен должен быть в .env или прописан здесь вручную
    token = os.getenv("YOUGILE_TOKEN", "YOUR_TOKEN_HERE")
    return YougileProjects(base_url, token)


