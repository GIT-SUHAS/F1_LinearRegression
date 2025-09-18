import pandas as pd

df1 = pd.read_csv(r'/Users/suhasbajjuri/Desktop/f1_ML_project/f1 dataset, from 1950 to 2024/formula-1-world-championship-history-1950-2024/versions/1/Qualifying_Results.csv')

#print(df1.head())

df2 = pd.read_csv(r"/Users/suhasbajjuri/Desktop/f1_ML_project/f1 dataset, from 1950 to 2024/formula-1-world-championship-history-1950-2024/versions/1/Race_Results.csv")

#print(df2.head())

print(df1.columns)