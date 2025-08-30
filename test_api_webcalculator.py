import requests
import pytest

# Тестирование основных операций калькулятора


@pytest.mark.parametrize(
    "operation, x, y, expected",
    [
        ("addition", 10, 5, 15),
        ("multiplication", 10, 5, 50),
        ("division", 10, 5, 2),
        ("remainder", 10, 5, 0),
    ],
)
def test_api_functional(calculator_server, operation, x, y, expected):
    payload = {"x": x, "y": y}
    response = requests.post(f"http://localhost:17678/api/{operation}",
                             json=payload)
    data = response.json()
    assert data["statusCode"] == 0
    assert data["result"] == expected
