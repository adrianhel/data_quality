import great_expectations as gx
import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()

#print(df.dtypes)

# PassengerId      int64
# Survived         int64
# Pclass           int64
# Name            object
# Sex             object
# Age            float64
# SibSp            int64
# Parch            int64
# Ticket          object
# Fare           float64
# Cabin           object
# Embarked        object
# dtype: object

#print(df['Cabin'])

# 0       NaN
# 1       C85
# 2       NaN
# 3      C123
# 4       NaN
#        ...
# 886     NaN
# 887     B42
# 888     NaN
# 889    C148
# 890     NaN
# Name: Cabin, Length: 891, dtype: object


df_ge = gx.from_pandas(df)
df_ge.head()

