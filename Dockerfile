# docker build -t covid19 .

FROM python:3.8

WORKDIR /code

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE $PORT

CMD gunicorn -w 10 -b 0.0.0.0:8080 -t 100000 --max-requests 20 web:server

#CMD ["python", "./web.py"]


# To run: docker run -it --name covid19 --rm -p 8050:8050 covid19