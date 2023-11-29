FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY mnist /app/mnist
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
