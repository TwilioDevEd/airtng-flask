FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python3 -m venv venv && . venv/bin/activate

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

RUN python3 manage.py db upgrade

CMD ["python3", "manage.py", "runserver"]
