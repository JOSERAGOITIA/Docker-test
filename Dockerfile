FROM python:3.10.5

ADD test.py .
ADD data.csv . 

#ADD . /DOCKER-TEST/Transaction.csv 

#WORKDIR /Docker-test

COPY requirements.txt . 



RUN pip install -r requirements.txt


CMD [ "python","./test.py"]


