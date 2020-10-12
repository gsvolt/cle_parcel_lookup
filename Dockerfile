FROM python:3.7.3-apline3.9

LABEL Author="Gaurav Narain Saxena"
LABEL Email="gsvolt7@gmail.com"
LABEL version="1.0"

ENV FLASK_APP "/app/cle_parcel_lookup"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True 

WORKDIR /app

COPY . .

RUN apk update && \
    apk upgrade && \
    apk add bash && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade --trusted-host pypi.python.org -r requirements-dev.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0