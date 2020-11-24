#-*-coding:utf-8 -*-
# txt to csv


import csv


csvFile = open("data/A.txt", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("./data2/A.txt",'r',encoding='utf-8')
for line in f:
    csvRow = line.split()
    # print(csvRow[1:])
    writer.writerow(csvRow[1:])

f.close()
csvFile.close()

