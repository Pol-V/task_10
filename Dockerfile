FROM python:3.8-slim

COPY requirements.txt .
WORKDIR .
RUN pip install -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
