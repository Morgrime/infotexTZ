import requests


# проверка состояния сервера
def test_state_response_format(calculator_server):
    response = requests.get("http://localhost:17678/api/state")

    # статус сервера
    assert response.status_code == 200

    data = response.json()
    # есть ли нужные поля
    assert "statusCode" in data
    assert "state" in data

    # проверка типов возвращаемых данных
    assert type(data["statusCode"]) is int
    assert type(data["state"]) is str

    # сервер возвращает "OК" (латинская O + кириллическая К). хитро
    assert data["state"] == "OК"


# Сложение x и y
def test_addition_response_format(calculator_server):
    payload = {"x": 10, "y": 5}
    response = requests.post(
        "http://localhost:17678/api/addition", json=payload
    )

    # статус сервера
    assert response.status_code == 200

    data = response.json()
    # есть ли нужные поля
    assert "statusCode" in data
    assert "result" in data

    # проверка типов возвращаемых данных
    assert type(data["statusCode"]) is int
    assert type(data["result"]) is int


# Умножение x и y
def test_multiplication_response_format(calculator_server):
    payload = {"x": 10, "y": 5}
    response = requests.post(
        "http://localhost:17678/api/multiplication", json=payload
    )

    # статус сервера
    assert response.status_code == 200

    data = response.json()
    # есть ли нужные поля
    assert "statusCode" in data
    assert "result" in data

    # проверка типов возвращаемых данных
    assert type(data["statusCode"]) is int
    assert type(data["result"]) is int


# Деление на цело x на y
def test_division_response_format(calculator_server):
    payload = {"x": 10, "y": 5}
    response = requests.post(
        "http://localhost:17678/api/division", json=payload
    )

    # статус сервера
    assert response.status_code == 200

    data = response.json()
    # есть ли нужные поля
    assert "statusCode" in data
    assert "result" in data

    # проверка типов возвращаемых данных
    assert type(data["statusCode"]) is int
    assert type(data["result"]) is int


# Остаток от деления x на y
def test_remainder_response_format(calculator_server):
    payload = {"x": 10, "y": 5}
    response = requests.post(
        "http://localhost:17678/api/remainder", json=payload
    )

    # статус сервера
    assert response.status_code == 200

    data = response.json()
    # есть ли нужные поля
    assert "statusCode" in data
    assert "result" in data

    # проверка типов возвращаемых данных
    assert type(data["statusCode"]) is int
    assert type(data["result"]) is int
