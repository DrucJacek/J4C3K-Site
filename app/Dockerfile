FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 
ENV PYTHONDONTWRITEBYTECODE=1 
ENV UV_PROJECT_ENVIRONMENT="/venv"
ENV PATH="/venv/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock ./

COPY . .

RUN uv sync --frozen

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
