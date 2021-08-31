FROM python:3.7

ENV PYTHONUNBUFFERED 1

EXPOSE 8080

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH=/app
WORKDIR /app



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]