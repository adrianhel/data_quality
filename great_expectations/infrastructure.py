import great_expectations as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# выводим в качестве проверки:
# список типов данных
print(df.dtypes)

# количество занятых мест по каютам
print(df['Cabin'])


# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()