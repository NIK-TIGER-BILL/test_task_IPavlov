# Тестовое задание для компании IPavlov
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=FastAPI)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)  
  
Задание выполнялось для компании IPavlov  
Документация с описанием API:  
http://localhost/docs  
http://localhost/redoc  

## Для запуска проекта
* Склонировать репозиторий на локальную машину:
```
https://github.com/NIK-TIGER-BILL/test_task_IPavlov
```
* Переименовать файл с перменными окружения .env_template на .env. И заполнить на свое усмотрение:  
```
DB_ENGINE=<postgresql>  
DB_NAME=<имя базы данных postgres>  
DB_USER=<пользователь бд>  
DB_PASSWORD=<пароль>  
DB_HOST=<db>  
DB_PORT=<5432>  
```
* Соберите docker-compose:  
```
docker-compose up -d --build
```
* Примените миграции:
```
docker-compose exec web alembic upgrade head
```
* Для отключения пропишите:  
```
docker-compose up -d --build
```
