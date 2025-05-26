from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student_success():
    response = client.post("/students", json={
        "name": "Alice",
        "age": 21,
        "grade": "A"
    })
    print("Create Response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student added"
    assert data["data"]["name"] == "Alice"
    assert data["data"]["age"] == 21
    assert data["data"]["grade"] == "A"

def test_get_all_students():
    response = client.get("/students")
    print("All Students:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_student_by_id_success():
    response = client.get("/students/0")
    print("Get by ID Success:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"

def test_get_student_by_id_invalid():
    response = client.get("/students/999")
    print("Get by ID Invalid:", response.json())
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_update_student_success():
    response = client.put("/students/0", json={
        "name": "Alice Updated",
        "age": 22,
        "grade": "A+"
    })
    print("Update Response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student updated"
    assert data["data"]["name"] == "Alice Updated"
    assert data["data"]["age"] == 22

def test_partial_update_student():
    response = client.patch("/students/0", json={
        "grade": "A++"
    })
    print("Partial Update Response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == "Student partially updated"
    assert data["data"]["grade"] == "A++"

def test_delete_student():
    response = client.delete("/students/0")
    print("Delete Response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student deleted"
    assert "name" in data["data"]

def test_search_student_found():
    client.post("/students", json={"name": "Bob", "age": 20, "grade": "B"})
    response = client.get("/search?name=Bob")
    print("Search Found:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert any(s["name"] == "Bob" for s in data["results"])

def test_search_student_not_found():
    response = client.get("/search?name=Unknown")
    print("Search Not Found:", response.json())
    assert response.status_code == 200
    assert response.json()["results"] == []

def test_check_dependency():
    response = client.get("/check")
    print("Check Dependency:", response.json())
    assert response.status_code == 200
    assert response.json() == {"note": "Common dependency injected"}

def test_options_students():
    response = client.options("/students")
    print("Options Response:", response.json())
    assert response.status_code == 200
    assert "allowed_methods" in response.json()

def test_head_students():
    response = client.head("/students")
    print("Head Response Status Code:", response.status_code)
    assert response.status_code in [200, 204]
