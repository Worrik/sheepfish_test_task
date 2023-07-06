# Test task

1. Set env variables in .env (copy .env-example).
2. Run postgres, redis and wkhtmltopdf using docker
```bash
docker compose up -d
```
3. Update ports of redis and wkhtmltopdf urls in .env (get from `docker ps`).
4. `poetry install` or `pip install -r requirements.txt`.
5. `python manage.py runserver`.
6. `celery -A proj worker -l INFO`.
