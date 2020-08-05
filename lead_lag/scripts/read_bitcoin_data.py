import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore', message='numpy.dtype size changed')
warnings.filterwarnings('ignore', message='numpy.ufunc size changed')


def read_small_data(small_filename):
    # print(f'Reading {small_filename}')
    d = pd.read_csv(small_filename, parse_dates=True, index_col=0)
    # returns data in centiseconds
    d['timestamp'] = d.index.values.astype(np.int64) // 10 ** 7
    return d


def bitcoin_data(exchange_1_small_data_file, exchange_2_small_data_file):
    exchange_1 = read_small_data(exchange_1_small_data_file)
    exchange_2 = read_small_data(exchange_2_small_data_file)

    return exchange_1[['timestamp', 'last']].values, exchange_2[['timestamp', 'last']].values

def bitcoin_data_v2(exchange_1_small_data_file, exchange_2_small_data_file):
    exchange_1 = read_small_data(exchange_1_small_data_file)
    exchange_2 = read_small_data(exchange_2_small_data_file)

    exchange_1_columns = list(exchange_1.columns)
    exchange_2_columns = list(exchange_2.columns)

    return exchange_1[[exchange_1_columns[1], exchange_1_columns[0]]].values, exchange_2[[exchange_2_columns[1], exchange_2_columns[0]]].values

def bitcoin_data_v2_filtered(exchange_1_small_data_file, exchange_2_small_data_file, start_date, end_date):
    exchange_1 = read_small_data(exchange_1_small_data_file).between_time(start_date.time(), end_date.time())
    exchange_2 = read_small_data(exchange_2_small_data_file).between_time(start_date.time(), end_date.time())

    exchange_1_columns = list(exchange_1.columns)
    exchange_2_columns = list(exchange_2.columns)

    return exchange_1[[exchange_1_columns[1], exchange_1_columns[0]]].values, exchange_2[[exchange_2_columns[1], exchange_2_columns[0]]].values
