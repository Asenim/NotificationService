### Описание
Сервис уведомлений с JWT аутентификацией

#### Используемые технологии
- python
- FastAPI
- Docker
- Docker-compose
- Postgres
- Redis
- Tortoise ORM

### .env
```dotenv
# Подключение к postgres
POSTGRES_USER=value
POSTGRES_PASSWORD=value
POSTGRES_DB=db_name
DB_HOST=postgres
DB_PORT=5432

# Подключение к redis
REDIS_HOST=redis
REDIS_PORT=6379

AVATAR_URL=hardcode

# Алгоритм и соль для JWT
JWT_SECRET=supersecret_change_me
JWT_ALG=HS256

# Время жизни Токенов в минутах
ACCESS_JWT_EXPIRE_MINUTES=10
REFRESH_JWT_EXPIRE_MINUTES=20
```
### Запуск
#### Простой и быстрый способ
После того как сделаете
```shell
git pull
```
Переходите в папку проекта
```shell
cd имя папки проекта
```
Создаете файл `.env`  

Поднимаете проект
```shell
docker-compose -f docker-compose.yaml up
```

#### Второй способ
```shell
git pull
```
```shell
git cd папка спуленного проекта
```
Не забываем про `.env`   
В pycharm обязательно ПКМ по папке спуленного проекта -> Mark Directory as -> Sources root 
Поднимаем контейнеры с окружением  
Далее поднимаем БД и редис   
```shell
docker-compose -f docker-compose.dev.yaml up
```
Запускаем приложение либо из pycharm либо из консоли  
```shell
python src/main.py
```

### Запросы
Для локальных запросов лучше использовать postman app установленный на компьютер  
Что бы начать отправлять запросы  
После того как запустили приложение, переходим в postman app
Во вкладку `collections`
Нажимаем `New`  
Для `post` запросов обязательно выбираем вкладку `raw` (А не `FormData`)  
И в поле вставляем наши jsonы для запросов  

Примеры запросов будут ниже

#### Регистрация
- Пример запроса  
POST http://127.0.0.1:8080/auth/register  
body `{"username": "value"}`  

- Успех
```JSON
{
    "id": 1,
    "access_token": "str",
    "refresh_token": "str"
}
```

- Юзер с таким `username` Существует
```JSON
{
    "detail": "User with this username already exists"
}
```

#### Авторизация
- Пример запроса  
POST: http://127.0.0.1:8080/auth/login  
body: `{"username": "value"}`  

- Успех
```JSON
{
    "access_token": "str",
    "refresh_token": "str"
}
```

- Если Юзера не существует
```JSON
{
    "detail": "User not found"
}
```

#### Создание уведомлений

POST http://127.0.0.1:8080/notifications  
Headers Authorization Bearer <Token>  
body `{"type": "like", "text": "str"}`  
P.S. "type" может быть только "comment", "like" или "repost"  

- Успех
```JSON
{
    "user_id": 1,
    "type": "like",
    "text": "str"
}
```
- Неудача
```JSON
{
    "detail": "Not authenticated"
}
```
```json
{
    "detail": "Invalid token"
}
```
#### Удаление своих уведомления
DELETE http://127.0.0.1:8080/notifications/id  
Headers Authorization Bearer <Token>  

- Успех
```JSON
{
    "user_id": 1,
    "notification_id": 1,
    "detail": "Notification deleted"
}
```
- Неудача
```JSON
{
    "detail": "Notification not found"
}
```
```JSON
{
    "detail": "Invalid token"
}
```
```JSON
{
    "detail": "Not authenticated"
}
```

#### Получение списка уведомлений
GET http://127.0.0.1:8080/notifications
Headers Authorization Bearer <Token>  
QueryParams limit, offset Пример строки ?limit=10&offset=10  

- Успех
```JSON
{
    "user": "username avatar_url",
    "notifications": [
        {
            "type": "like",
            "text": "10"
        },
        {
            "type": "like",
            "text": "10"
        },
        {
            "type": "like",
            "text": "10"
        }
    ]
}
```
- Неудача
```JSON
{
    "detail": "Invalid token"
}
```
```JSON
{
    "detail": "Not authenticated"
}
```
