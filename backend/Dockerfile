FROM python:3.10-slim

RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["./entrypoint.sh"]
