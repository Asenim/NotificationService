FROM python:3.10

WORKDIR /notification-service

COPY requirements.txt .
RUN pip install -v --upgrade pip && pip install -v -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
