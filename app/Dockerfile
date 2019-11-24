FROM python:3.6
MAINTAINER Sripathi Kammari "kammari.sripathi@gmail.com"
COPY src /src
WORKDIR /src
EXPOSE 5000
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
