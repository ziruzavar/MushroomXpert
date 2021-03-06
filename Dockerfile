FROM python:3.7.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/