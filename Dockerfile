FROM python:3.6-alpine

ADD decoder.py /

CMD [ "python", "./decoder.py" ]