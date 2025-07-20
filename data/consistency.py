import great_exp as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()


# 4. СОГЛАСОВАННОСТЬ
# на примере колонки "Pclass"
# класс билета пассажира может быть 1, 2 или 3
# воспользуемся методом "expect_column_values_to_be_between"

check4_Pclass = df_ge.expect_column_values_to_be_between(
    column = 'Pclass',
    min_value = 1,
    max_value = 3
)

print('check4_Pclass: ', check4_Pclass)  # увидим всю информацию

if not check4_Pclass['success']:                       # увидим только информацию из "result" при условии,
    print('check4_Pclass: ', check4_Pclass['result'])  # что проверка выдаст "success": false
# Вывод пуст, значит данные в колонке "Pclass" согласованны.