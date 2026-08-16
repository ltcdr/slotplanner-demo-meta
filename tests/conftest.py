import sys
from pathlib import Path
import pytest


# --- PATH SETUP --------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]

SERVICE_ROOT = ROOT / "services" / "slotplanner-demo"
DEMO_ROOT = SERVICE_ROOT / "demo"
BACKEND_ROOT = DEMO_ROOT / "backend"

sys.path.append(str(ROOT))
sys.path.append(str(SERVICE_ROOT))
sys.path.append(str(DEMO_ROOT))
sys.path.append(str(BACKEND_ROOT))


# --- IMPORT FASTAPI APP ------------------------------------------------------
from services.slotplanner_demo.demo.backend.main import app

from fastapi.testclient import TestClient


# --- FIXTURES ----------------------------------------------------------------
@pytest.fixture
def client():
    return TestClient(app)


class FakeSession:
    def commit(self): pass
    def rollback(self): pass
    def close(self): pass


@pytest.fixture
def mock_db(monkeypatch):
    def fake_get_db():
        yield FakeSession()

    monkeypatch.setattr(
        "services.slotplanner_demo.demo.backend.db.get_db",
        fake_get_db
    )


@pytest.fixture
def env(monkeypatch):
    monkeypatch.setenv("SLOTPLANNER_ENV", "test")
