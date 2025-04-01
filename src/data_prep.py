import numpy as np
import pandas as pd
from py7zr import SevenZipFile
import os
import io
from config import data_path


read_path = os.path.join(data_path, 'SPY_options')
df = pd.DataFrame()

for filename in os.listdir(read_path):
    if filename.endswith('.7z'):
        with SevenZipFile(os.path.join(read_path, filename), 'r') as archive:
            for txt_name, data in archive.readall().items():
                if txt_name.endswith('.txt'):
                    with io.TextIOWrapper(data) as f:
                        temp_df = pd.read_csv(f, sep=',', header=0, low_memory=False)
                        df = pd.concat([df, temp_df], ignore_index=True)

col = [x.strip() for x in df.columns]
col = [x.strip('[]') for x in col]
df.rename(columns=dict(zip(df.columns, col)), inplace=True)

df = df.drop(['QUOTE_UNIXTIME', 'QUOTE_READTIME', 'QUOTE_TIME_HOURS', 'EXPIRE_UNIX'], axis=1)
str_cols = df.select_dtypes(include=['object']).columns
df[str_cols] = df[str_cols].apply(lambda c: c.str.strip()).replace('', np.nan)
df['QUOTE_DATE'] = pd.to_datetime(df['QUOTE_DATE'])
df['EXPIRE_DATE'] = pd.to_datetime(df['EXPIRE_DATE'])
float_cols = df.columns.difference(['QUOTE_DATE', 'EXPIRE_DATE', 'EXPIRE_UNIX', 'C_SIZE', 'P_SIZE'])
df[float_cols] = df[float_cols].astype('float64')

df = df[[
    'QUOTE_DATE', 'UNDERLYING_LAST', 'EXPIRE_DATE', 'DTE', 'STRIKE', 'STRIKE_DISTANCE', 'STRIKE_DISTANCE_PCT',
    'C_BID', 'C_ASK', 'C_SIZE', 'C_LAST', 'C_DELTA', 'C_GAMMA', 'C_VEGA', 'C_THETA', 'C_RHO', 'C_IV', 'C_VOLUME',
    'P_BID', 'P_ASK', 'P_SIZE', 'P_LAST', 'P_DELTA', 'P_GAMMA', 'P_VEGA', 'P_THETA', 'P_RHO', 'P_IV', 'P_VOLUME'
]]

save_path = os.path.join(data_path, 'SPY_options.parquet')
df.to_parquet(save_path)
