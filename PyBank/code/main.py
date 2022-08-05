# 

import os
import csv

csv_path = os.path.join('..', 'Resources', 'budget_data.csv')
# csv_path = 'D:\\UCIBootcamp\\Module3_challenge\\python_challenge\\PyBank\\Resources\\budget_data.csv'
# 


total_month = 0
net_amount = 0
date = []
changes = []
profit_change_list = []
profit_change_list_2 =[]

# decrease =  []
# 
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # find the total amount
    for row in csvreader:
        #calculate total row
        total_month += 1
        #calculate total change in budget
        net_amount = net_amount + int(row[1])
        date.append(row[0])

        changes.append(int(row[1]))
    for i in range(1, len(changes)):

        profit_change_list.append(changes[i]-changes[i-1])

        # calculate average change
        avg_profit = round(sum(profit_change_list)/len(profit_change_list),2)


        # point out max min in profit
        max_profit = max(profit_change_list)
        min_profit = min(profit_change_list)
        # return date have max/min profit
        great_profit_increase = profit_change_list.index(max(profit_change_list)) + 1
        great_profit_decrease = profit_change_list.index(min(profit_change_list)) + 1
print("Financial Analysis")
print("--------------------")        
print("Total months: ", total_month)
print("Total: $",net_amount)
print(f'Average Change: ${avg_profit}')    
print(f'Greatest Increase in Profit:  {date[great_profit_increase]} ${max_profit}')
print(f'Greatest Decrease in Profit:  {date[great_profit_decrease]} ${min_profit}')

output = os.path.join('..', 'analysis', 'analysis_summary.txt')
with open(output, 'w') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("-------------------")
    txtfile.write("\n")
    txtfile.write(f'Total months: {total_month}')
    txtfile.write("\n")
    txtfile.write(f'Total: ${net_amount}')
    txtfile.write("\n")
    txtfile.write(f'Average Change: ${avg_profit}')
    txtfile.write("\n")    
    txtfile.write(f'Greatest Increase in Profit:  {great_profit_increase} ${max_profit}')
    txtfile.write("\n")
    txtfile.write(f'Greatest Decrease in Profit:  {great_profit_decrease} ${min_profit}')