Inspired by - https://github.com/ArjanCodes/2022-docker 

### Fastapi

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Build and run the Docker image locally:

```
docker build -t channel-api -f build-fastapi/Dockerfile .
docker run -d -p 8080:80 channel-api
docker ps
docker kill d5f...
```

In order to run the server with docker compose:

```
docker-compose -f build-fastapi/docker-compose.yaml up --build
```

If you use docker compose, and you make a minor change in the file, you can now see how everything is updated and the server is restarted automatically

### Flask

```
docker build -t channel-flask -f build-flask/Dockerfile .
```

```
docker run -p 5000:5000 channel-flask
```

```
docker-compose -f build-flask/docker-compose.yaml up --build
```

### GraphQL vs REST
flask-api-main vs flask-graphql-main
