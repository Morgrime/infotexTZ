import subprocess
import pytest
import os


# Находим путь к текущей директории (где лежит conftest.py)
CURRENT_DIR = os.path.dirname(__file__)

# Путь к webcalculator.exe в той же папке
CALC_PATH = os.path.join(CURRENT_DIR, "webcalculator.exe")


# нужна для запуска сервера
@pytest.fixture
def calculator_server():
    process = subprocess.Popen(
        [CALC_PATH, "start", "localhost", "17678"],
    )

    yield  # здесь выполняются тесты

    try:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
