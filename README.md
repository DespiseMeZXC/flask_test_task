# flask_test_task

## install project
```
uv sync
```
## activate venv
```
source .venv/bin/activate
```

## run project
```
uv run python src/main.py
```

##test cases

###request creating data
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"Мне нравится этот сервис, он хороший"}' http://localhost:5000/reviews
```
### response on request
```
{
  "created_at": "2025-07-08T14:02:02.875588+00:00",
  "id": 6,
  "sentiment": "positive",
  "text": "\u041c\u043d\u0435 \u043d\u0440\u0430\u0432\u0438\u0442\u0441\u044f \u044d\u0442\u043e\u0442 \u0441\u0435\u0440\u0432\u0438\u0441, \u043e\u043d \u0445\u043e\u0440\u043e\u0448\u0438\u0439"
}
```

### request get data with param ?sentiment=positive
```
curl -X GET "http://localhost:5000/reviews?sentiment=positive"
```
### response on request
```
[
  {
    "created_at": "2025-07-08T13:01:33.091126",
    "id": 1,
    "sentiment": "positive",
    "text": "\u041c\u043d\u0435 \u043d\u0440\u0430\u0432\u0438\u0442\u0441\u044f \u044d\u0442\u043e\u0442 \u0441\u0435\u0440\u0432\u0438\u0441, \u043e\u043d \u0445\u043e\u0440\u043e\u0448\u0438\u0439"
  },
  {
    "created_at": "2025-07-08T13:42:08.628975+00:00",
    "id": 2,
    "sentiment": "positive",
    "text": "\u041c\u043d\u0435 \u043d\u0440\u0430\u0432\u0438\u0442\u0441\u044f \u044d\u0442\u043e\u0442 \u0441\u0435\u0440\u0432\u0438\u0441, \u043e\u043d \u0445\u043e\u0440\u043e\u0448\u0438\u0439"
  },
]
```
### request get data without param
```
curl -X GET http://localhost:5000/reviews
```
### response on request
```
[
    все записи в бд
]
```
