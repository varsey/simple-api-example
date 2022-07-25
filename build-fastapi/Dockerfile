FROM python:3.9.7-slim

WORKDIR /app

COPY build-fastapi/requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["uvicorn", "fastapi-main:app", "--host", "0.0.0.0", "--port", "80"]