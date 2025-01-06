# Конфигурация проекта с dishka
## Важные ссылки
Видео про DIP, DI, Dishka, FastAPI - [Dishka + FastAPI | Пиши код правильно](https://youtu.be/CJo3Fs_hgws?si=NPNLCs5DHS4Vc8HY) \
Телеграм канал с полезной информацией - [Паша в мире АйТи](https://t.me/+S_xBkK-a0go4N2Iy)
## Как запустить? 
1. Создать вирутальное окружение\
```python -m venv venv```
2. Активировать виртуальное окружение \
К примеру, на unix системе:
```source venv/bin/activate```
3. Установить зависимости \
```pip install -r requirements.txt```
4. Создать файл .env и добавить *SOME_STRING* \
К примеру, ```SOME_STRING=from_env_hello```
5. Запустить при помощи точки входа \
```PYTHONPATH=src uvicorn app.run:make_app```
