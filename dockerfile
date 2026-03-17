FROM python:3.11

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app .

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]