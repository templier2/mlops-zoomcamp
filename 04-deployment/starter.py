#!/usr/bin/env python
# coding: utf-8
import sys
import pickle
import pandas as pd


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


year = int(sys.argv[1])
month = int(sys.argv[2])
df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')

dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)
print(f"Mean for {month:02d}/{year:04d} is {y_pred.mean()}")
