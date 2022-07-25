FROM python:3.9.7-slim

WORKDIR /app

COPY build-flask/requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["python3", "flask-main.py"]