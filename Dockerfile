FROM  python:3.8



WORKDIR /application

copy . /application


RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["APP.py"]
