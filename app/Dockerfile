FROM python:3.6
MAINTAINER Sripathi Kammari "kammari.sripathi@gmail.com"
COPY src /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]