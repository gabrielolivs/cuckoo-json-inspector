FROM python:3.11-slim

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "main.py"]

CMD ["-f", "/data/report.json", "--menu"]
