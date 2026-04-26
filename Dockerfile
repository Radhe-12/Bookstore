FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask gunicorn

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "app:app"]