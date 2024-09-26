FROM python:3.12-slim

WORKDIR /workspace/

RUN pip install fastapi uvicorn jinja2 --no-cache-dir

COPY ./src /workspace/src

WORKDIR /workspace/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]