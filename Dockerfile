FROM python:3.10

ENV PYTHONNUNBUFFER=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

RUN echo "python manage.py makemigrations" >> start.sh
RUN echo "python manage.py migrate" >> start.sh
RUN echo "python manage.py collectstatic --noinput" >> start.sh
RUN echo "python manage.py runserver 0.0.0.0:8080" >> start.sh
RUN chmod +x start.sh

# Set the shell script as the final CMD to execute
CMD [ "./start.sh" ]