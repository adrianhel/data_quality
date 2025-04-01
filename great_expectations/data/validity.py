import great_expectations as gx
import pandas as pd


# считываем данные
df = pd.read_csv('titanic.csv')
df.head()

# создаем объект датафрейма GE (библиотека ожиданий)
df_ge = gx.from_pandas(df)
df_ge.head()


# 3. ВАЛИДНОСТЬ
# на примере колонки "Sex"
# пол может быть либо male, либо female
# воспользуемся методом "expect_column_values_to_match_regex"

check3_Sex = df_ge.expect_column_values_to_match_regex(
    column = 'Sex',
    regex = '^male$|^female$'  # регулярное выражения
)

print('check3_Sex: ', check3_Sex)  # так мы увидим полный результат нашей проверки
# "success": true

if not check3_Sex['success']:                    # если проверка не пройдена, то мы увидим результаты
    print('check3_Sex: ', check3_Sex['result'])  # проверки без лишней информации
# Вывод пуст, значит проверка на валидность данных в столбце Sex пройдена успешно — данные валидны.