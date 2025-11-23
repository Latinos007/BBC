import pandas as pd
import numpy as np

#1 открытие файла
dp = pd.read_csv("tested.csv")

print("#1.2\nналичие пропусков")
print(dp.isna().sum(), "\n\n")

print("признаки и их характер")
print(dp.dtypes, '\n\n')

print("#1.3 первые 5 строк")
print(dp.head(), "\n\n")

print("№1.4 базовая статистика по столбцам")
for col in dp.columns:
    if dp[col].dtype in ["int64", "float64"]:
        #print(col, dp[col].min(), dp[col].max(), dp[col].mean(), dp[col].median(), sep='|    |')
        print(dp[col].describe(), end='\n\n')
print("\n\n")

print("#1.5 кол-во заголовков и строк")
print(f'кол-во строк:{dp.shape[0]}; столбцов {dp.shape[1]}\n\n')

#1.6 замена пропусков возраста на среднее
mean_Age = dp["Age"].mean()
dp["Age"] = dp['Age'].fillna(mean_Age)

#2.1 сравнение М и Ж
print('процент выживших М:', dp[(dp["Sex"] == "male") & (dp["Survived"] == 1)].shape[0] / dp[dp["Sex"] == "male"].shape[0])
print('процент выживших Ж:', dp[(dp["Sex"] == "female") & (dp["Survived"] == 1)].shape[0] / dp[dp["Sex"] == "female"].shape[0])

print('средний возраст:', dp["Age"].mean())
print('средний возраст погибших М:', dp[(dp["Sex"] == "male")]["Age"].mean())
print('средний возраст выживших Ж:', dp[(dp["Sex"] == "female") & (dp["Survived"] == 1)]["Age"].mean(), end='\n\n')

#2.2
print('мужчиный старше 30 1 класс:')
print(dp[(dp["Sex"] == 'male') & (dp['Age'] > 30) & (dp['Pclass'] == 1)], end='\n\n')

print('выжившие женщины и дети')
print(dp[((dp["Sex"] == 'female') | (dp['Age'] < 18)) & (dp['Survived'] == 1)], end='\n\n')

dp_sc = dp.groupby(['Sex', 'Pclass'])
print('\nсредний возраст:')
print(dp_sc['Age'].mean())
print('\nдоля выживших:')
print(dp_sc['Survived'].value_counts())
print('\nсредняя цена билета:')
print(dp_sc['Fare'].mean())

dp.to_csv('new_tested.csv', index=False)