# django-stripe-API
## Установка
Создайте clone:
```
git clone https://github.com/EXTRAS12/django-stripe-API.git/
```
Создайте в папке виртуальное окружение и запустите:
python3 -m venv venv

Перейдите в корневой каталог проекта:
``` 
cd core
```

И установите зависимости: 
```
pip install -r requirements.txt
```


Вы можете протестировать возможности проекта на предоставленной **тестовой** базе данных
(**Суперюзер**: Логин:admin Пароль:admin или удалить файл **db.sqlite3** и подключить свою базу данных.

Для **теста** функционала с тестовой базой данных:
```
python manage.py runserver
```

После подключения **своей или новой** базы данных:
```
python manage.py migrate
python manage.py createsuperuser
```
В случае **ошибки** удалите файл main/migrations/0001_inital.py:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Или просто запустите команду
```
docker-compose up
