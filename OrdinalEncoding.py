import pandas as pd

df_org = pd.read_csv('data.csv')
df = df_org.copy()

category_order = ['Never', 'Rarely', 'Most Days', 'Everyday']
df['Breakfast_encoded'] = 'Unknown'


for id, category in df['Breakfast'].items():
    df.loc[id, 'Breakfast_encoded'] = category_order.index(category)

print(df)
