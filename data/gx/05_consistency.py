import great_expectations as gx
import pandas as pd


df = pd.read_csv('titanic.csv')

df_ge = gx.from_pandas(df)


check4_Pclass = df_ge.expect_column_values_to_be_between(
    column = 'Pclass',
    min_value = 1,
    max_value = 3
)
print('check4_Pclass: ', check4_Pclass)

if not check4_Pclass['success']:
    print('check4_Pclass: ', check4_Pclass['result'])