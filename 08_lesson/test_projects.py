import pytest
import uuid


def unique_title():
    return f"Project_{uuid.uuid4().hex[:8]}"


# --- [POST] Создание проекта ---
def test_create_project_positive(api):
    payload = {"title": unique_title()}
    response = api.create_project(payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_no_title(api):
    payload = {}  # Обязательное поле title отсутствует
    response = api.create_project(payload)
    assert response.status_code >= 400


# --- [GET] Получение проекта ---
def test_get_project_positive(api):
    # Создаем проект, чтобы его прочитать
    res_create = api.create_project({"title": unique_title()}).json()
    project_id = res_create["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_not_found(api):
    fake_id = str(uuid.uuid4())
    response = api.get_project(fake_id)
    assert response.status_code == 404


# --- [PUT] Обновление проекта ---
def test_update_project_positive(api):
    res_create = api.create_project({"title": "Old Title"}).json()
    project_id = res_create["id"]

    new_title = unique_title()
    response = api.update_project(project_id, {"title": new_title})
    assert response.status_code == 200

    # Проверка через GET
    updated_data = api.get_project(project_id).json()
    assert updated_data["title"] == new_title


def test_update_project_negative_invalid_id(api):
    response = api.update_project("invalid-id", {"title": "New"})
    assert response.status_code >= 400

