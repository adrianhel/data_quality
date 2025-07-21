import great_expectations as gx
import pandas as pd


df = pd.read_csv('titanic.csv')

df_ge = gx.from_pandas(df)


check3_Sex = df_ge.expect_column_values_to_match_regex(
    column = 'Sex',
    regex = '^male$|^female$'
)
print('check3_Sex: ', check3_Sex)


if not check3_Sex['success']:
    print('check3_Sex: ', check3_Sex['result'])