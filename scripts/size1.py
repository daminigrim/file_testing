import pandas as pd

for i,chunk in enumerate(pd.read_csv(r'compair_file\2023-01-16.csv', chunksize=852208)):
    chunk.to_csv('chunk(25){}.csv'.format(i), index=False)