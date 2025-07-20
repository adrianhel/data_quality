import great_expectations as gx
import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()

print(f"Список типов данных:\n{df.dtypes}")

print(f"Список типов данных:\n{df['Cabin']}")

#df_ge = gx.from_pandas(df)
#df_ge.head()