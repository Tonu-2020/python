import csv
with open('t.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['1'], row['2'])