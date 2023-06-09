# Консольный сокращатель ссылок

Скрипт который позволяет сократить ссылку через консоль. Работает через API
Bitly. Так же есть возможность посмотреть общее количество кликов по ранее созданной
ссылке. 

## Установка

---

Для начала необходимо создать новое виртуальное окружение:

```shell-session
python -m venv </path/to/new/virtual/environment>
source </path/to/new/virtual/environment>/bin/activate
```

Затем установить зависимости командой:

```shell
pip install -r requirements.txt
```
Установятся библиотеки [requests](https://pypi.org/project/requests/) и 
[python-dotenv](https://pypi.org/project/python-dotenv/), и все зависимости.

Также необходимо получить токен Bitly API [страница генерации токена](https://app.bitly.com/settings/api/)
необходима регистрация. 

Далее переименуйте файл `.envexample` в `.env` и вставьте полученный вами токен.


## Описание работы скрипта

---
Для получения короткой ссылки введите в командной строке находясь в папке проекта:

```shell
python main.py https://google.com/
```
Пример корректной работы скрипта:
```
(venv) ➜  console_bitly_link_shortener git:(main) ✗ python main.py https://google.com
Битлинк, https://bit.ly/3KfSRZY
```
Пример выдачи общего количества кликов по битлинку за все время:
```
(venv) ➜  console_bitly_link_shortener git:(main) ✗ python main.py https://bit.ly/3KfSRZY
Всего кликов: 2
```