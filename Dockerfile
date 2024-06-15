FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "test"]
