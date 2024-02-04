FROM python:3.9.6

ENV PYTHONUNBUFFERED 1

WORKDIR /app

#COPY requirements.txt .

#RUN pip3 install -r requirements.txt
RUN pip install Django==3.2.9
RUN pip install psycopg2-binary 
RUN pip install djangorestframework 


COPY . /app/

EXPOSE 8000

ENTRYPOINT [ "/app/django.sh"]


