FROM python:3
WORKDIR /usr/src/todo
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    libpq-dev \
    gcc \
    g++
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt