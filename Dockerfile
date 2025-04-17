# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip --no-cache-dir && pip install -r requirements.txt

COPY . /app/

EXPOSE 80
CMD ["gunicorn", "recipes_project.wsgi:application", "--bind", "0.0.0.0:80"]