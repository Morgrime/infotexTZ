
# Тесты для WebCalculator


## Зависимости

Для запуска тестов необходимы следующие пакеты Python:

- `pytest` — запуск тестов
- `requests` — HTTP-запросы к серверу
- `pytest-html` — автогенерация отчёта в формате HTML 

Установить зависимости можно командой:

```sh
pip install pytest requests pytest-html
```

## Запуск тестов

1. Убедитесь, что файл `webcalculator.exe` находится в той же папке, что и тесты.
2. Запустите тесты командой:

```sh
pytest --html=report.html
```

После завершения тестирования будет создан файл `report.html` с подробным отчётом.

## Структура тестов

- `test_api_webcalculator.py` — базовые арифметические операции
- `test_base_functional.py` — формат ответов и типы данных
- `test_negative.py` — негативные сценарии и обработка ошибок
- `test_management_functional.py` — управление сервером (start/stop/restart)
- `conftest.py` — фикстуры для запуска сервера