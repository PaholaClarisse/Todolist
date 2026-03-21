from fastapi.testclient import TestClient
from Todolist import app # Assure-toi que ton fichier s'appelle bien main.py

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200