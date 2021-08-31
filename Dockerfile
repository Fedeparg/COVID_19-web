# docker build -t covid19 .

FROM python:3.8

WORKDIR /code

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE $PORT

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--max-requests", "20", "web:server"]

#CMD ["python", "./web.py"]


# To run: docker run -it --name covid19 --rm -p 8080:8080 covid19