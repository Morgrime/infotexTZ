# tests/test_negative.py
import pytest
import requests

# Все операции, принимающие {"x", "y"}
OPERATIONS = ["addition", "multiplication", "division", "remainder"]


# проверка всех действий на работу с отсутствующим ключом
@pytest.mark.parametrize("operation", OPERATIONS)
def test_missing_keys(calculator_server, operation):
    payload = {"x": 10}
    response = requests.post(f"http://localhost:17678/api/{operation}", json=payload)

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] == 2
    assert "statusMessage" in data
    assert isinstance(data["statusMessage"], str)


# проверка всех действий на работу с float данными вместо int
@pytest.mark.parametrize("operation", OPERATIONS)
def test_non_integer_value(calculator_server, operation):
    payload = {"x": 10.5, "y": 5}
    response = requests.post(f"http://localhost:17678/api/{operation}", json=payload)

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] == 3
    assert "statusMessage" in data


# проверка всех действий на работу с str данными вместо int
@pytest.mark.parametrize("operation", OPERATIONS)
def test_string_value(calculator_server, operation):
    payload = {"x": "abc", "y": 5}
    response = requests.post(f"http://localhost:17678/api/{operation}", json=payload)

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] == 3
    assert "statusMessage" in data


# проверка всех действий на работу с данными за рамками int32
@pytest.mark.parametrize("operation", OPERATIONS)
def test_out_of_int32_range(calculator_server, operation):
    payload = {"x": 3000000000, "y": 5}
    response = requests.post(f"http://localhost:17678/api/{operation}", json=payload)

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] == 4
    assert "statusMessage" in data


# проверка всех действий на работу с пустым JSON
@pytest.mark.parametrize("operation", OPERATIONS)
def test_empty_body(calculator_server, operation):
    response = requests.post(f"http://localhost:17678/api/{operation}", json={})

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] in [2, 5]
    assert "statusMessage" in data


# проверка всех действий на работу с чем-то вместо JSON
@pytest.mark.parametrize("operation", OPERATIONS)
def test_invalid_json_format(calculator_server, operation):
    response = requests.post(
        f"http://localhost:17678/api/{operation}",
        data="это не JSON",
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code in [200, 400, 415]

    if response.headers.get("Content-Type", "").startswith("application/json"):
        data = response.json()
        assert data["statusCode"] == 5
        assert "statusMessage" in data


# проверка деления на 0
@pytest.mark.parametrize("operation", ["division", "remainder"])
def test_division_by_zero(calculator_server, operation):
    payload = {"x": 10, "y": 0}
    response = requests.post(f"http://localhost:17678/api/{operation}", json=payload)

    assert response.status_code in [200, 400]
    data = response.json()

    assert data["statusCode"] == 8  # возвращает код 8, вместо код 1 (ошибка вычисления)
    assert "statusMessage" in data
