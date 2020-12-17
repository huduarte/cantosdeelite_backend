FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# Passa ao container a porta escolhida para o projeto e a expoe para o host (default:8000)
ARG PORT
EXPOSE $PORT