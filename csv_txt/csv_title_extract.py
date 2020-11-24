import csv
import pandas as pd


df = pd.read_csv("./data/new.csv")

b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
for i in range(len(df)):
    a = "fail"
    if a in df.loc[i, 'Result']:
        a1 = df.loc[i, 'Domain']
        a2 = df.loc[i, 'Semantic']
        a3 = df.loc[i, 'Expect Slot']
        a4 = df.loc[i, 'Result']
        a5 = df.loc[i, 'Actual Slot']
        b1.append(a1)
        b2.append(a2)
        b3.append(a3)
        b4.append(a4)
        b5.append(a5)

f1 = pd.DataFrame(columns=['Domain', 'Semantic', 'Expect Slot', 'Result', 'Actual Slot'])
f1['Domain'] = b1
f1['Semantic'] = b2
f1['Expect Slot'] = b3
f1['Result'] = b4
f1['Actual Slot'] = b5
# print(f1)
# f1.to_csv('fail.csv_txt', sep=',', index=False, encoding="utf-8")
f1.to_excel('fail.xlsx', index=False)

# print(f2)
f2 = f1[f1['Domain'].isin(["周边"])]
# f2.to_csv('fail_周边.csv_txt', sep=',', index=False, encoding="utf-8")
f2.to_excel('fail_周边.xlsx', index=False)

