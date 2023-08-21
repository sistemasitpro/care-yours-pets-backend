# Dockerfile for Python app
FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]
