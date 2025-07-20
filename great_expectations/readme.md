# Great Expectations

[![Python](https://img.shields.io/badge/python-3.11.0-blue?logo=pypi)](https://www.python.org/downloads/release/python-3110/)
[![Pandas](https://img.shields.io/badge/pandas-blue?logo=pandas)]()
[![GX](https://img.shields.io/badge/great-expectations-blue)](https://github.com/great-expectations)

### [Назад в Data Quality ⤶](/README.md)

___

<img src="/img/cover.png" width="100%">

## О проекте
Изучим **некоторые** возможности по очистке данных на датасете **Титаник**.

## Используемый в проекте датасет
- [Титаник](data/titanic.csv)

## Содержание
1. **[Инфраструктура](data/infrastructure.md)**:
_Подгружаем библиотеку и датасет._  
2. **[Полнота](data/completeness.py)**: 
_Проверяем датафрейм на наличие пустых значений в колонках._  
3. **[Уникальность](data/uniqueness.py)**:
_Проверяем датафрейм на количество уникальных значений в колонках._  
4. **[Достоверность](data/validity.py)**:
_Проверяем насколько данные отвечают определенным требованиям._  
5. **[Согласованность](data/consistency.py)**:
_Проверяем на принадлежность данных определенным диапазонам/правилам._  

## Используемые инструменты
- **Pandas**  

> ***Pandas*** — это мощная библиотека для анализа и обработки данных в Python.

- **Great Expectations**

> ***Great Expectations (GX)*** — это опенсорсный инструмент на основе Python для управления качеством данных.  

**GX** предоставляет возможность профилировать и тестировать данные, а также составлять по ним отчёты.
  
 ---  
Больше информации по библотеке [Great Expectations](https://github.com/great-expectations).