import pytest
from fastapi.testclient import TestClient
from usher.front.server.__main__ import app  # Adjust import based on actual app location

client = TestClient(app)

# Test cases for POST /messages/
def test_post_message_valid():
    response = client.post("/messages/", json={"issue_id": "ABC-123", "status": "test"})
    assert response.status_code == 201

    response = client.post("/messages/", json={"issue_id": "DEF-456", "status": "stage"})
    assert response.status_code == 201

def test_post_message_invalid_issue_id():
    response = client.post("/messages/", json={"issue_id": "ABC123", "status": "test"})
    assert response.status_code == 422

def test_post_message_invalid_status():
    response = client.post("/messages/", json={"issue_id": "ABC-123", "status": "deployed"})
    assert response.status_code == 422

def test_post_message_missing_issue_id():
    response = client.post("/messages/", json={"status": "test"})
    assert response.status_code == 422

# Test cases for GET /messages/
def test_get_messages_valid_project_name():
    # Preload messages in the queue before testing
    client.post("/messages/", json={"issue_id": "ABC-123", "status": "test"})
    client.post("/messages/", json={"issue_id": "DEF-456", "status": "stage"})
    
    response = client.get("/messages/?project_name=ABC")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["issue_id"] == "ABC-123"

def test_get_messages_valid_status():
    response = client.get("/messages/?status=test")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["issue_id"] == "ABC-123"

def test_get_messages_no_matches():
    response = client.get("/messages/?project_name=XYZ")
    assert response.status_code == 404

# Test cases for DELETE /messages/
def test_delete_messages_valid():
    client.post("/messages/", json={"issue_id": "ABC-123", "status": "test"})
    response = client.delete("/messages/?project_name=ABC")
    assert response.status_code == 200
    assert response.json()["count"] == 1

def test_delete_messages_no_matches():
    response = client.delete("/messages/?project_name=XYZ")
    assert response.status_code == 404