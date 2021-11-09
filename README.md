# Practice Python

Practice-python is a simple Fast api project for dealing with modern rest api technologies.




## Deployment with docker

Go to the project root directory and run:

```bash
docker-compose up -d --build
```

## Run local

### Prepare environment and install dependencies

```
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### Run server


```
uvicorn app.main:app --reload

```

## Web routes
All routes are available on /docs paths with Swagger.
