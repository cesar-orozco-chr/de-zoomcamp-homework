import pandas as pd
import argparse
import os
import time
from sqlalchemy import create_engine

def download_csv(url, dest_file='source.csv'):

    import requests
    d = requests.get(url)
    with open(dest_file,'w') as f:
        f.write(d.text)

    return dest_file

def main(params):
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', 'root')
    taxi_file = download_csv(params.url)
    db_host = params.host
    db_port = params.port
    db_name = params.database
    db_table = params.table
    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    df_iter = pd.read_csv(taxi_file, iterator=True, chunksize=100000)
    t_start = time.perf_counter()
    df = next(df_iter)
    df.head(n=0).to_sql(db_table, engine, if_exists='replace')
    df.to_sql(db_table, engine, if_exists='append')
    t_end = time.perf_counter()
    print(f"Inserted chunk ... Took {t_end - t_start:0.4f} seconds")

    try:
        while True:
            t_start = time.perf_counter()
            df = next(df_iter)
            df.to_sql(db_table, engine, if_exists='append')
            t_end = time.perf_counter()
            print(f"Inserted chunk ... Took {t_end - t_start:0.4f} seconds")
    except StopIteration:
        print("All set!")
    
    


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str,
                        help="Postgres host server")
    parser.add_argument("--port", type=str,
                        help="Postgres server port")
    parser.add_argument("--database", type=str,
                        help="Postgres database name")            
    parser.add_argument("--table", type=str,
                        help="Postgres table name")
    parser.add_argument("--url", type=str,
                        help="Postgres table name")
    args = parser.parse_args()

    main(args)