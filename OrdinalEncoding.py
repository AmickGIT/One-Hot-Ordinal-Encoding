import pandas as pd
import numpy as np

df_org = pd.read_csv('data.csv')
df = df_org.copy()

category_order = np.array(['Never', 'Rarely', 'Most Days', 'Everyday'])
df['Breakfast_encoded'] = 'Unknown'


for id, category in df['Breakfast'].items():
    index = np.where(category_order == category)[0]
    if index.size > 0:
        df.loc[id, 'Breakfast_encoded'] = index[0]
    
df.to_csv('data_ordinal.csv')
print(df)
