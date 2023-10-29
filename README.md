## Тестовое задание для вакансии "Backend программист" компании HighTech Plant

## Требования:
Создать веб-приложение c использованием фреймворка Django.
Приложение должны быть авторизованы следующие функции:
- авторизация/регистрация через адрес электронной почты+пароль с подтверждением адреса электронной почты
- страница со списком пользователей
- страница профиля пользователя
- страница редактирования профиля
- сброс пароля
- изменение пароля
- изменение адреса электронной почты

Дополнительные требования:
- Данное веб-приложение должно иметь возможность запуска через docker-compose на Windows/Linux/MacOS
- При разработке необходимо использовать СУБД Postgres.
- Идентификаторы пользователей должны быть в формате UUID4.
- Выложить приложение в GIT





## Изменения:

### 0.0.0 
Создан репозиторий


### 0.0.1
Проверка работы удаленного репозитория 

### 0.0.2
- Создан проект.
- Установлен dotenv. 
- Спрятан SECRET_KEY. 
- Создан .gitignore.
- Занесены файлы и директории в gitignore.


### 0.0.3
- Создано приложение accounts
- Создана модель MyUser c id формата UUID4
- Настроена БД PostgreSQL

### 0.0.3.1
- Исправлены некоторые ошибки


### 0.0.4
- создан шаблон base.html
- созданы шаблон и представление списка пользователей
- созданы шаблон и представление страницы входа
- прикручен Bootstrap
- реализована пагинация списка пользователей

### 0.0.5 
- Создан шаблон и представление user_detail
- реализован метод get_absolute_url модели MyUser

### 0.0.6
- Внесены изменения в модель MyUser: теперь поле is_active по умолчанию False, поле email обязательно и уникально. 
 Необходимо для реализации подтверждения почты

### 0.0.7
- Реализовано подтверждение электронной почты

### 0.0.8
- Реализована страница редактирования профиля
- реализовано изменение адреса электронной почты с подтверждением
- реализовано изменение пароля

### 0.0.9 
- релизован сброс пароля
