import great_expectations as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()


# 1. ПОЛНОТА
# Проверим датафрейм на наличие пустых значений в колонках,
# чтобы понять, с какими из них стоит работать.
# Если в колонке большой процент значений NaN/Null, значит
# данные не качественные.

# на примере колонки "Cabin"
# воспользуемся методом "expect_column_values_to_not_be_null"

check1_Cabin = df_ge.expect_column_values_to_not_be_null(   # "значение колонки не Null"
    column = 'Cabin', # название исследуемой колонки
    mostly = 0.25   # пороговое значение, говорящее, что "как минимум 25% должно быть не Null"
)

#print('check1_Cabin: ', check1_Cabin)

# В result:
# — "element_count" это размер нашего датафрейма,
# — "unexpected_count" это количество Null значений,
# — "unexpected_percent" процент Null значений в колонке от общего числа записей в df,
# — "partial_unexpected_list" это список значений, которые не удовлетворяют условимям проверки,
# NaN/Null туда не пишется, ибо это "пустота"

if not check1_Cabin['success']:
    print(check1_Cabin['result'])


# на примере колонки "Ticket"
check1_Ticket = df_ge.expect_column_values_to_not_be_null(
    column = 'Ticket',
    mostly = 0.99
)

#print('check1_Ticket: ', check1_Ticket)

if not check1_Ticket['success']:
    print(check1_Ticket['result'])

# никакого вывода, т.к. абсолютно для всех строк присутствует значение в колонке "Ticket"