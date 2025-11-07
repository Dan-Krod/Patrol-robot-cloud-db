FROM python:3.10-slim

WORKDIR /app

COPY load_test.py .

RUN pip install requests

CMD ["python", "load_test.py"]
