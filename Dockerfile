FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
RUN pip install gunicorn


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]