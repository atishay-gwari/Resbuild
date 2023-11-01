FROM python:3.10

ENV PYTHONNUNBUFFER=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080


CMD [ "python","manage.py", "runserver","0.0.0.0:8080" ]