#!/bin/bash
URL=http://192.168.20.102:9000/yellow_tripdata_2021-01.csv

docker run -it \
  --network=pg-network \
  ingest_taxi_data:001 \
    --host=pg-database \
    --port=5432 \
    --database=taxi_trips \
    --table=yellow_cabs \
    --url=${URL}