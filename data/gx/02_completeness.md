# 2. Полнота

### [Назад в Содержание ⤶](/data/gx.md)

## 2.1 Проверка на отсутствие значений на примере колонки `Cabin`
Если в колонке большой процент значений _NaN/Null_, значит данные не качественные.
На примере колонки `Cabin` воспользуемся методом `expect_column_values_to_not_be_null`:

```python
check1_Cabin = df_ge.expect_column_values_to_not_be_null(   # "значение колонки не Null"
    column = 'Cabin',  # название исследуемой колонки
    mostly = 0.25      # пороговое значение, говорящее, что "как минимум 25% должно быть не Null"
)
print('check1_Cabin: ', check1_Cabin) # так мы увидим полный результат нашей проверки
```

<img src="/img/gx_2.1.png" width="40%">

Если `success`: _true/false_ — проверка пройдена/не пройдена.

В `result`:
- `element_count` это размер нашего датафрейма,
- `unexpected_count` это количество Null значений,
- `unexpected_percent` процент _Null_ значений в колонке от общего числа записей в _df_,
- `partial_unexpected_list` это список значений, которые не удовлетворяют условимям проверки, _NaN/Null_ туда не пишется, 
ибо это _пустота_

```python
if not check1_Cabin['success']:     # удобная конструкция, если проверка не пройдена, то мы увидим
    print(check1_Cabin['result'])   # результаты проверки без лишней информации
```

<img src="/img/gx_2.2.png" width="100%">

## 2.2 Проверка на отсутствие значений на примере колонки `Ticket`
Повторим на примере другой колонки.

```python
check1_Ticket = df_ge.expect_column_values_to_not_be_null(
    column = 'Ticket',
    mostly = 0.99
)
print('check1_Ticket: ', check1_Ticket) # так мы увидим полный результат нашей проверки
```

<img src="/img/gx_2.3.png" width="40%">

```python
if not check1_Ticket['success']:     # если проверка не пройдена, то мы увидим результаты
    print(check1_Ticket['result'])   # проверки без лишней информации
```

Здесь мы не увидим никакого вывода, т.к. абсолютно для всех строк присутствует значение в колонке `Ticket`.

## 2.3 Код
- [Полнота (код)](02_completeness.py)