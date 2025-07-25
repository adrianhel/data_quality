# 1. Инфраструктура
Подгружаем библиотеку и датасет.  

### [Назад в Содержание ⤶](/data/gx.md)

## 1.1 Установка необходимых библиотек
Для работы должен быть установлен **Python** версии **3.11.9**.

Устанавливаем библиотеку ожиданий (вместе с ней установится и pandas):

```bash
pip install great_expectations==0.18.11
```

## 1.2 Импорт библиотек и проверка датасета
- Импортируем библиотеки:

```python
import great_expectations as gx
import pandas as pd
```

- Считываем данные:

```python
df = pd.read_csv('titanic.csv')
print(df.head())
```

<img src="/img/gx_1.1.png" width="50%">  

- Выводим в качестве проверки список типов данных:

```python
print(df.dtypes)
```

<img src="/img/gx_1.2.png" width="20%">  

- Выводим в качестве проверки количество занятых мест по каютам:

```python
print(df['Cabin'])
```

<img src="/img/gx_1.3.png" width="34%">  

Первое, что бросается в глаза, это наличие значений **NaN** (это отсутствие какого-либо значения) в колонке `Cabin`.  

Это плохо и работать с такими данными не очень бы хотелось. Поэтому мы проверим наш датафрейм и
воспользуемся библиотекой **Great Expectations**.


- Создаем объект датафрейма библиотеки GX (библиотека ожиданий):  

Применяем метод _from_pandas_ к _pandas_-датафрейму поверх библиотеки _GX_. К нему можно применять все те же методы, 
которые можно применять к _pandas_-датафрейму, но также можно будет применять все методы библиотеки GX.

```python
df_ge = gx.from_pandas(df)
print(df_ge.head())
```

<img src="/img/gx_1.4.png" width="50%">  

## 1.3 Код
- [Инфраструктура (код)](01_infrastructure.py)