FROM python:3.11-slim

WORKDIR /app
COPY process.py .

CMD ["python", "process.py"]