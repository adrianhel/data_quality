import great_expectations as gx
import pandas as pd


df = pd.read_csv('titanic.csv')

df_ge = gx.from_pandas(df)


check2_Ticket = df_ge.expect_column_values_to_be_unique(
    column = 'Ticket',
    mostly = 0.99
)
print('check2_Ticket: ', check2_Ticket)


if not check2_Ticket['success']:
    print(check2_Ticket['result'])


print(df[df["Ticket"] == "113803"])


check2_Name = df_ge.expect_column_values_to_be_unique(
    column = 'Name',
    mostly = 0.99
)
print('check2_Name: ', check2_Name)


if not check2_Name['success']:
    print(check2_Name['result'])