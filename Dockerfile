FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN pip install --upgrade pip && pip install uv
RUN uv pip install --system --no-cache-dir -e .

ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
