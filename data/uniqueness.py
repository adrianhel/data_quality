import great_exp as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()


# 2. УНИКАЛЬНОСТЬ
# на примере колонки "Ticket"
# предположим, что каждый едет по своему билету
# воспользуемся методом "expect_column_values_to_be_unique"

check2_Ticket = df_ge.expect_column_values_to_be_unique(
    column = 'Ticket',
    mostly = 0.99
)

print('check2_Ticket: ', check2_Ticket) # так мы увидим полный результат нашей проверки

if not check2_Ticket['success']:
    print(check2_Ticket['result'])
# при mostly = 0.99 вывод будет, при 0.5 — нет, соответственно

# Видим вывод, значит проверка не пройдена.
# — "element_count" - количество строк датафрейма,
# — "missing_count",
# — "missing_percent",
# — "unexpected_count" - количество неуспешных проверок,
# — "unexpected_percent_total" - процент неуспешных проверок,
# — "partial_unexpected_list" - примеры билетов, которые имеют дубликаты.

# Проверим билет 113803
print(df[df["Ticket"] == "113803"])
# видим две записи по одному билету, судя по именам, это семья плыла по одному билету,
# это нормально для данного датасета, поэтому изменим mostly с 0.99 на 0.5


# Повторим проверку на примере колонки "Name",
# предположим, что каждый едет по своему билету.

check2_Name = df_ge.expect_column_values_to_be_unique(
    column = 'Name',
    mostly = 0.99
)

print('check2_Name: ', check2_Name) # так мы увидим полный результат нашей проверки

if not check2_Name['success']:
    print(check2_Name['result'])
# Вывод пуст, дублей имен нет.