import great_expectations as gx
import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()

print(df.dtypes)

print(df['Cabin'])

df_ge = gx.from_pandas(df)
df_ge.head()