# PollProject
# API для системы проведения опросов

Клонируйте репозиторий.

Выполните команду `docker-compose -f docker-compose-example.yaml up --build`

Проект будет работать на `127.0.0.1`

Документация написана собственноручно с помощью OpenAPI 3.0.3

После деплоя доступна по адресу `127.0.0.1/docs/`


    Функционал для администратора системы:
      - Авторизация в системе
      - Добавление/изменение/удаление опросов.
        Атрибуты опроса: название, дата старта, дата окончания, описание.
        После создания поле "дата старта" у опроса менять нельзя
      - Добавление/изменение/удаление вопросов в опросе.
        Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

    Функционал для пользователей системы:
      - Получение списка активных опросов
      - Прохождение опроса.
        Опросы можно проходить анонимно, один пользователь может участвовать в любом количестве опросов
      - Получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID    уникальному пользователя
