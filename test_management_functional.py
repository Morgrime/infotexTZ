import subprocess
import requests
import time


CALC_PATH = r"C:\Users\User\Desktop\ТЗ\webcalculator.exe"
PAUSE_TIME = 3


# не работает с впном (выруби)
def test_start_with_default_settings():
    process = subprocess.Popen(
        [CALC_PATH, "start"],
    )

    time.sleep(PAUSE_TIME)

    try:
        response = requests.get("http://127.0.0.1:17678/api/state")
        assert response.status_code == 200
        data = response.json()
        assert data["statusCode"] == 0
    finally:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
        process.wait(timeout=5)


def test_start_with_base_port():
    process = subprocess.Popen(
        [CALC_PATH, "start", "localhost"],
    )

    time.sleep(PAUSE_TIME)

    try:
        response = requests.get("http://localhost:17678/api/state")
        assert response.status_code == 200
        data = response.json()
        assert data["statusCode"] == 0
    finally:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
        process.wait(timeout=5)


def test_start_with_custom_port():
    process = subprocess.Popen(
        [CALC_PATH, "start", "localhost", "5678"],
    )

    time.sleep(PAUSE_TIME)

    try:
        response = requests.get("http://localhost:5678/api/state")
        assert response.status_code == 200
        data = response.json()
        assert data["statusCode"] == 0
    finally:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
        process.wait(timeout=5)


def test_restart_process():
    process = subprocess.Popen(
        [CALC_PATH, "start", "localhost", "5678"],
    )

    time.sleep(PAUSE_TIME)

    try:
        response = requests.get("http://localhost:5678/api/state")
        assert response.status_code == 200
        data = response.json()
        assert data["statusCode"] == 0

        subprocess.run([CALC_PATH, "restart"], timeout=10)
        time.sleep(PAUSE_TIME)

        response_after = requests.get("http://localhost:5678/api/state")
        assert response_after.status_code == 200
        data_after = response_after.json()
        assert data_after["statusCode"] == 0

    finally:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
        process.wait(timeout=5)


def test_stop_process():
    process = subprocess.Popen(
        [CALC_PATH, "start", "localhost", "5678"],
    )

    time.sleep(PAUSE_TIME)

    try:
        response = requests.get("http://localhost:5678/api/state")
        assert response.status_code == 200
        data = response.json()
        assert data["statusCode"] == 0
    finally:
        subprocess.run([CALC_PATH, "stop"], timeout=5)
        process.wait(timeout=5)
