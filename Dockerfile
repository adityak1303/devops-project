FROM python:3.10
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
CMD ["env", "FLASK_APP=.", "FLASK_ENV=production", "python", "-m", "flask", "run"]
