### Установка зависимостей

$ pip install -r requirements.txt
### Allure
pip install allure-pytest
### Запуск тестов и создание отчета

pytest tests --alluredir allure_results

### Отчет в allure

allure serve allure_results
[README.md](README.md)