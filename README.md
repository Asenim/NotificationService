### Описание

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
docker-compose up
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

#### Удаление своих уведомления
#### Получение списка уведомлений
