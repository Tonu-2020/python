import csv
f=open('t.csv','rt')
#rint(f.readlines())
myreader = csv.reader(f)
for row in myreader:
   print(row)