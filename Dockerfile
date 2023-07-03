FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN export FLASK_APP=server.py
CMD ["flask", "run", "--host=0.0.0.0"]
