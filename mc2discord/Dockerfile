FROM python:3.7-alpine
RUN apk add --update tini
ENTRYPOINT ["/sbin/tini", "--"]

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD python chat.py
