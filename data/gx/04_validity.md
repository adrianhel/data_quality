# 4. Достоверность

### [Назад в Содержание ⤶](/data/gx.md)

## 4.1 На примере колонки "Sex"
Пол может быть либо _male_, либо _female_. Проверим, так ли это в нашем датасете.  
Воспользуемся методом `expect_column_values_to_match_regex`:  

```python
check3_Sex = df_ge.expect_column_values_to_match_regex(
    column = 'Sex',
    regex = '^male$|^female$'  # регулярное выражения
)
print('check3_Sex: ', check3_Sex)  # так мы увидим полный результат нашей проверки
```

<img src="/img/gx_4.1.png" width="40%">

`"success": true` — проверка пройдена.  

```python
if not check3_Sex['success']:                    # если проверка не пройдена, то мы увидим результаты
    print('check3_Sex: ', check3_Sex['result'])  # проверки без лишней информации
```

Вывод пуст, значит проверка на валидность данных в столбце `Sex` пройдена успешно — данные валидны.  

## 4.2 Код
- [Достоверность (код)](04_validity.py)