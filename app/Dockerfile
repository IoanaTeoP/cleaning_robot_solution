FROM python:3.13.1-slim
WORKDIR /app
RUN pip install --upgrade pip && pip install poetry
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/
RUN poetry install --without dev
COPY . /app
ENV PYTHONPATH "/"
CMD ["python", "cleaning_robot/main.py"]