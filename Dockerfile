FROM python:3.10.1-slim-buster

RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip
 # Setting Home Directory for containers
WORKDIR /app

# Installing python dependencies and copying app
COPY . /app

# requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt  

ENV PORT 8080
EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
