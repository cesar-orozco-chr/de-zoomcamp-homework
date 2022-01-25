#!/bin/bash
URL=http://192.168.20.102:9000/taxi_zones.csv

docker run -it \
  --network=pg-network \
  ingest_taxi_data:001 \
    --host=pg-database \
    --port=5432 \
    --database=taxi_trips \
    --table=zone \
    --url=${URL}