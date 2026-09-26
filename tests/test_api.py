import pytest
from fastapi.testclient import TestClient

import highscore_service
from main import app

client = TestClient(app)

def test_eintrag_speichern():
    antwort = client.post("/api/highscores", json={"name": "Isabel", "score": 100, "modus": "pro"})
    assert antwort.status_code == 201
    assert antwort.json()["modus"] == "pro"
