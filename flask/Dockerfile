FROM python:3.9-slim

WORKDIR /flask

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app /flask

CMD [ "python", "app/app.py"]