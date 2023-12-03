# CHAT

Проект представляет собой простую реализацию чата с использованием комнат. Реализован с использованием Websockets библиотеки Django-channels

## Установка


1. Клонируйте репозиторий: `git clone https://github.com/VadimP21/Chat.git`
2. Перейдите в каталог проекта: `cd Chat_with_Channels`
3. Установите зависимости: `pip install -r requirements.txt`


## Развертывание

Для запуска требуется установленные Docker, Docker-compose

1. Перейдите в каталог проекта: `cd Chat_with_Channels/`
2. Для запуска PostgresSQl выполнить: `docker-compose -f docker-compose.yml up -d`
3. Для запуска Redis выполнить: ` docker run --rm -p 6379:6379 redis:7`
4. Запустите сервер разработки: `python manage.py runserver`
5. Откройте браузер и перейдите по адресу: `http://127.0.0.1:8000/`


## Настройка окружения


Для удобства работы над проектом, рекомендуется использовать виртуальное окружение. Для этого выполните следующие команды:


1. Установите `virtualenv`, если он ещё не установлен: `pip install virtualenv`
2. Создайте виртуальное окружение: `virtualenv env`
3. Активируйте виртуальное окружение:
   - На Windows: `env\Scripts\activate`
   - На macOS и Linux: `source env/bin/activate`
4. Перейдите в каталог проекта: `cd Chat_with_Channels`
5. Создайте файл `.env`
6. Перенесите переменные окружения из образца `.env.example` в `.env`


##  Переменные окружения (описание в файле .env.example):


DEBUG='' # Режим Debug: bool

SECRET_KEY='' # Секретный код из settings

ALLOWED_HOSTS='' # Разрешенные хосты

POSTGRES_DB='' #  Название БД

POSTGRES_USER='' #  Пользователь БД

POSTGRES_PASSWORD='' #  Пароль для БД

DB_HOST='' #  Хост БД
