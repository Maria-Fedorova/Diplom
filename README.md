# Личный дневник

## Описание проекта

Приложение позволяет пользователям создавать, редактировать и удалять записи в дневнике,
а также просматривать свои записи в удобном интерфейсе.
Пользовательский интерфейс реализован с использованием Django шаблонов
и Bootstrap стилей с адаптивным и современным дизайном.

Записи формируются для конкретного пользователя. Другие пользователи не могут смотреть чужие записи и профили.

## Основные возможности

- Регистрация и аутентификация пользователей.
- Создание, редактирование и удаление записей.
- Возможность поиска записей по заголовку или содержимому в интерфейсе сайта.
- Пользователи могут просматривать список всех своих записей.
- Пользователи могут просматривать отдельные записи в подробном виде.

---

## Структура проекта

### Основные файлы и папки

- **`manage.py`** — точка входа для управления проектом.
- **`config`** — директория с настройками и маршрутизацией проекта:
    - `settings.py` — основные настройки проекта.
    - `urls.py` — главная маршрутизация приложения.
- **`diary`** — модуль для работы с дневником:
    - `models.py` — модели записей.
    - `views.py` — обработка запросов (представления).
    - `forms.py` — формы для взаимодействия с пользователем.
    - `templates` — шаблоны для отображения интерфейса.
    - `templatetags` — пользовательские теги для шаблонов.
- **`users`** — модуль для управления пользователями:
    - `management` — директория для кастомных команд: csu -создать админа, cu -создать пользователя, cu_di - создает
      пользователя и записи для теста.
    - `models.py` — модель пользователя (если переопределена).
    - `views.py` — обработка регистрации, логина и профилей.
    - `forms.py` — формы для входа и регистрации.
    - `templates` — шаблоны, связанные с пользователями.

---

## Настройка и запуск проекта

+ Создать файл .env в корне проекта с настройками, аналогичными *.env.sample*.
+ ``docker-compose up --build`` - пересобрать контейнеры
+ ``docker-compose up`` - запуск контейнеров

Если не используется docker

+ Создать файл .env в корне проекта с настройками, аналогичными *.env.sample*.
+ Установить виртуальное окружение с интерпретатором. В настройках укажите параметр ``runserver``
+ Установите зависимости ``pip install -r requirements.txt --no-cache-dir``
+ Для тестирования создайте админа и пользователя командами  ``python manage.py csu`` и ``python manage.py cu``
+ Примените миграции ``python manage.py migrate``
