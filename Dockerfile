FROM python:3.7

RUN pip install fastapi uvicorn mangum pydantic sqlalchemy psycopg2-binary

EXPOSE 8080

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]