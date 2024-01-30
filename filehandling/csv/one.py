import csv
fp=open('one.csv','r')
data=csv.reader(fp)
for i in data:
    for j in i:
        print(j,"\t",end='')
    print()