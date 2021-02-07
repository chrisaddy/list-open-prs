FROM python:3.8.5-slim

COPY pyproject.toml ./
COPY poetry.lock ./

RUN pip install poetry \
        && poetry config virtualenvs.create false \
        && poetry install --no-dev \
	&& rm pyproject.toml poetry.lock

COPY src/ ./

ENTRYPOINT ["python", "list_open_prs.py"]
