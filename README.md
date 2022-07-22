Inspired by - https://github.com/ArjanCodes/2022-docker 

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Build and run the Docker image locally:

```
docker build -t channel-api -d build/Dockerfile .
docker run -d -p 8080:80 channel-api
docker ps
docker kill d5f...
```

In order to run the server with docker compose:

```
docker-compose -f build/docker-compose.yaml up --build
```

If you use docker compose, and you make a minor change in the file, you can now see how everything is updated and the server is restarted automatically
