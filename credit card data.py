# This dataset is from kaggle, specifically: https://www.kaggle.com/datasets/najeebz/electronic-card-transactions-dec-2023-new-zealand.
# It contains credit card transactions from NZ between 2000-2023.

import pandas as pd
import numpy as np
import plotly.express as pt

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('electronic-card-transactions-december-2023-csv-tables.csv')
df.shape

df['Period']=pd.to_datetime(df['Period'].astype('string'))

chart = pt.pie(df[(df.Period.dt.year == 2023) & (df.UNITS == 'Dollars')], 
       values = 'Data_value', 
       names = 'Period', 
       title = 'Transactions per month in 2023'
       )

chart.show()

# next up: line chart showing transactions per month over years 200
