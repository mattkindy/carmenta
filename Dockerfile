FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python-pip -y
COPY ./web /web
WORKDIR /web
RUN pip install -r requirements.txt
ENV FLASK_APP /web/root.py
CMD ["flask", "run", "--host=0.0.0.0"]
