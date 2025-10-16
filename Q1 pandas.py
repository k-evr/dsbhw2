import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df.loc[df.index[::20],['Manufacturer','Model','Type']])