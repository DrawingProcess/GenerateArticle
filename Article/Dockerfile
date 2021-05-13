# syntax=docker/dockerfile:1
 FROM python:latest
 WORKDIR /app
 COPY . /app
 RUN pip install -r ./requirements.txt
 EXPOSE 3000
 CMD ["python", "server.py"]