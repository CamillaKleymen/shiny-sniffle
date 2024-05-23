FROM python:3.12
COPY . /news
WORKDIR /news
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]

