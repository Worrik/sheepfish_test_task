# Test task

1. Set env variables in .env (copy .env-example).
2. Run postgres, redis and wkhtmltopdf using docker
```bash
docker compose up -d
```
3. Update ports of redis and wkhtmltopdf urls in .env (get from `docker ps`).

