FROM python:3.10

RUN apt-get update

RUN pip install awscli

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY conf/ /conf/

COPY controllers/ /controllers/

COPY services/ /services/

COPY swagger/ /swagger/

COPY entrypoint.sh entrypoint.sh

ADD app.py .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8080
