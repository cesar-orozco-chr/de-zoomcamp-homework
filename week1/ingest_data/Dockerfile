FROM python:3.9.1

RUN pip install --upgrade pip && \
    pip install --no-cache psycopg2-binary==2.9.3 && \
    pip install --no-cache pandas==1.4.0 && \
    pip install --no-cache SQLAlchemy==1.4.31 && \
    pip install --no-cache requests==2.27.1

WORKDIR /app
COPY ingest_taxi_data.py ingest_taxi_data.py

ENTRYPOINT [ "python", "ingest_taxi_data.py" ]

