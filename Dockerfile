FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
#RUN pip install -r requirements.txt --upgrade --force-reinstall

CMD ["python3","app.py"]