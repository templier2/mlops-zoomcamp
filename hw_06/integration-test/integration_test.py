from datetime import datetime
import pandas as pd

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df = pd.DataFrame(data, columns=columns)

options = {
    'client_kwargs': {
        'endpoint_url': "http://localhost:4566"
    }
}
df.to_parquet(
    "s3://nyc-duration/yellow_tripdata_2023-01.parquet",
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)