FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --progress-bar off flask==2.2.5

EXPOSE 9999

CMD ["python3", "sample_app.py"]
