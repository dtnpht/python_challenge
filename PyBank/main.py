# 
# from distutils.util import change_root
# from msilib import change_sequence
import os
import csv

# 
# csv_path = os.path.join('..', 'Resources', 'budget_data.csv')
csv_path = 'D:\\UCIBootcamp\\Module3_challenge\\python_challenge\\PyBank\\Resources\\budget_data.csv'
# 


total_month = 0
net_amount = 0
max = 0
month = []
year = []
# increase = []
# decrease =  []
# 
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    rows = list(csvreader)

    #loop to group 
    # for i in range(1, len(rows)):
    #     if rows[i+1][0] != rows[i][0]:



    #group budget by year

    # find the total amount
    for row in csvreader:
        #calculate total row
        total_month += 1
        #calculate total change in budget
        net_amount = net_amount + int(row[1])
        #split month and year
        split_time = row[0].split("-")
        month.append(split_time[0])
        year.append(split_time[1])
       
        #group budget by year
        # latest = csvreader.sort_values('Date', ascending=False).groupby('year').nth(0)
        # print(latest)
        # if net_amount > max:
        #     max = net_amount
        #     print(max)
    
print("Financial Analysis")
print("--------------------")        
print("Total months: ", total_month)
print("Total: $",net_amount)    
# print(year)