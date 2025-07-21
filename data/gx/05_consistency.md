# 5. Согласованность

### [Назад в Содержание ⤶](/data/gx.md)

## 5.1 На примере колонки "Pclass"
Класс билета пассажира может быть 1, 2 или 3.  
Воспользуемся методом `expect_column_values_to_be_between`:

```python
check4_Pclass = df_ge.expect_column_values_to_be_between(
    column = 'Pclass',
    min_value = 1,
    max_value = 3
)
print('check4_Pclass: ', check4_Pclass)  # увидим всю информацию
```

<img src="/img/gx_5.1.png" width="40%">

```python
if not check4_Pclass['success']:                       # увидим только информацию из "result" при условии,
    print('check4_Pclass: ', check4_Pclass['result'])  # что проверка выдаст "success": false
```

Вывод пуст, значит данные в колонке "Pclass" согласованны.

## 5.2 Код
- [Согласованность (код)](05_consistency.py)