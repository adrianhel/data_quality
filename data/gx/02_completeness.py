import great_expectations as gx
import pandas as pd


df = pd.read_csv('titanic.csv')

df_ge = gx.from_pandas(df)

check1_Cabin = df_ge.expect_column_values_to_not_be_null(
    column = 'Cabin',
    mostly = 0.25
)
print('check1_Cabin: ', check1_Cabin)


if not check1_Cabin['success']:
    print(check1_Cabin['result'])


check1_Ticket = df_ge.expect_column_values_to_not_be_null(
    column = 'Ticket',
    mostly = 0.99
)
print('check1_Ticket: ', check1_Ticket)


if not check1_Ticket['success']:
    print(check1_Ticket['result'])