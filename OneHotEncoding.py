import pandas as pd

df_original = pd.read_csv('color.csv')
df = df_original.copy()

unique_colors = set()

for id, color in df['Color'].items():
    if color not in unique_colors:
        df[color] = 0
        unique_colors.add(color)

    df.loc[id, color] = 1

print(df)
df.to_csv('color_one-hot.csv')