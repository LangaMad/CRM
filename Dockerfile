FROM python:3.10

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt


COPY . /app
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
