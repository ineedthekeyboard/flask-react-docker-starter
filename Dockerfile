# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/webapp
WORKDIR /opt/services/webapp

# copy our project code
COPY . /opt/services/webapp/

# install our two dependencies
RUN pip install -r requirements.txt

CMD gunicorn --bind :8080 --chdir src server:server