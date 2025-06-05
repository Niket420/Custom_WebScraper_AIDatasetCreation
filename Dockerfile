FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python", "M5_main_orchestration.py"]

