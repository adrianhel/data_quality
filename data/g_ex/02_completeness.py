import great_expectations as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()


# 1. ПОЛНОТА
# Если в колонке большой процент значений NaN/Null, значит
# данные не качественные.

# на примере колонки "Cabin"
# воспользуемся методом "expect_column_values_to_not_be_null"

check1_Cabin = df_ge.expect_column_values_to_not_be_null(   # "значение колонки не Null"
    column = 'Cabin',  # название исследуемой колонки
    mostly = 0.25      # пороговое значение, говорящее, что "как минимум 25% должно быть не Null"
)

print('check1_Cabin: ', check1_Cabin) # так мы увидим полный результат нашей проверки
# "success": true/false — проверка пройдена/не пройдена

# В result:
# — "element_count" это размер нашего датафрейма,
# — "unexpected_count" это количество Null значений,
# — "unexpected_percent" процент Null значений в колонке от общего числа записей в df,
# — "partial_unexpected_list" это список значений, которые не удовлетворяют условимям проверки,
# NaN/Null туда не пишется, ибо это "пустота"

if not check1_Cabin['success']:     # удобная конструкция, если проверка не пройдена, то мы увидим
    print(check1_Cabin['result'])   # результаты проверки без лишней информации


# Повторим на примере другой колонки — "Ticket"
check1_Ticket = df_ge.expect_column_values_to_not_be_null(
    column = 'Ticket',
    mostly = 0.99
)

print('check1_Ticket: ', check1_Ticket) # так мы увидим полный результат нашей проверки

if not check1_Ticket['success']:     # если проверка не пройдена, то мы увидим результаты
    print(check1_Ticket['result'])   # проверки без лишней информации

# Здесь мы не увидим никакого вывода, т.к. абсолютно для всех строк присутствует значение в колонке "Ticket".