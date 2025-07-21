# 3. Уникальность
Проверяем датафрейм на количество уникальных значений в колонках.  

### [Назад в Содержание ⤶](/data/gx.md)

## 3.1 На примере колонки "Ticket"
Предположим, что каждый едет по своему билету.  
Воспользуемся методом `expect_column_values_to_be_unique`:

```python
check2_Ticket = df_ge.expect_column_values_to_be_unique(
    column = 'Ticket',
    mostly = 0.99
)
print('check2_Ticket: ', check2_Ticket) # так мы увидим полный результат нашей проверки
```

<img src="/img/gx_3.1.png" width="40%">  
<img src="/img/gx_3.2.png" width="40%">  

В `result`:  
- `element_count` - количество строк датафрейма,  
- `missing_count` - количество отсутствующих значений,  
- `missing_percent` - процент отсутствующих значений,  
- `unexpected_count` - количество неуспешных проверок,  
- `unexpected_percent_total` - процент неуспешных проверок,  
- `partial_unexpected_list` - список билетов, которые имеют дубликаты.  

Более компактный вывод:

```python
if not check2_Ticket['success']:
    print(check2_Ticket['result'])
```

<img src="/img/gx_3.3.png" width="100%">

При `mostly = 0.99` вывод будет, при `0.5` — нет, соответственно.  
Видим вывод, значит проверка **не пройдена**.  

### Проверим билет №`113803`

```python
print(df[df["Ticket"] == "113803"])
```

<img src="/img/gx_3.4.png" width="44%">  

Видим две записи по одному билету, судя по именам (можно увидеть при полном выводе), это семья плыла по одному билету, 
это нормально для данного датасета, поэтому изменим `mostly` с `0.99` на `0.5`.  

## 3.2 Повторим проверку на примере колонки "Name"
Предположим, что каждый едет по своему билету.

```python
check2_Name = df_ge.expect_column_values_to_be_unique(
    column = 'Name',
    mostly = 0.99
)
print('check2_Name: ', check2_Name) # так мы увидим полный результат нашей проверки
```

<img src="/img/gx_3.5.png" width="40%">

```python
if not check2_Name['success']:
    print(check2_Name['result'])
```

Вывод пуст, дублей имен нет.

## 3.3 Код
- [Уникальность (код)](03_uniqueness.py)