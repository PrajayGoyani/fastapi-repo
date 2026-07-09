FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Run the app directly with Uvicorn (more explicit; binds to all interfaces so ports mapping works).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# below code is taken from here: https://fastapi.tiangolo.com/deployment/docker/
# CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]