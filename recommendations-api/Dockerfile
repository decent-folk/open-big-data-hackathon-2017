FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./src/* /app/
COPY recommendations.txt /app/recommendations.txt
WORKDIR /app
RUN pip install -r recommendations.txt
ENV FLASK_APP=/app/server.py
CMD flask run --host=0.0.0.0

