Dragon IT

задача минэнерго

## Требования

- Установить [Docker](https://www.docker.com/products/docker-desktop)
- `git clone https://github.com/urands/cp2020.git`

## Запуск сервера

Перейти в папку проекта:

```bash
docker-compose build
docker-compose up -d
```

Открываем наше приложение: [http://127.0.0.1](http://127.0.0.1)


## Остановка сервера

```bash
docker-compose down
```

### Запуск backend отдельно

```bash
#запустить образ
docker-compose up backend -d
```

### Запуск backend

```bash
#запустить образ
docker-compose down
```
