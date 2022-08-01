# Get started
import os
import csv
# 
import collections
# 
csv_path = 'D:\\UCIBootcamp\\Module3_challenge\\python_challenge\\PyPoll\\Resources\\election_data.csv'
# csv_path = os.path.join("..", "Resources", "election_data.csv")
# 
total_voters = 0
result = []
number_vote = 0
percent_vote = []
list_candidate = []

# 
with open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # 
    for row in csvreader:
        total_voters += 1
        candidates = row[2]
        list_candidate.append(candidates)
        
    # I use collection library to find all duplicates appear in csv file into a dictionary  
    dict_candidate = {key:value for key, value in collections.Counter(list_candidate).items() if value > 1}
    # I already check by print out all keys, and values in list I create above
    # So I know there are only 3 candidates in this election

    # I make a list to store names of candidates
    candidate_name = list(dict_candidate.keys())
    # I make a list to store all votes for each candidate
    dict_candidate_value = list(dict_candidate.values())
    
    
    # I calculate the percent vote of each candidate
    # And store them into a list for percent vote
    for i in dict_candidate_value:
        percent_vote.append(round((i/total_voters)*100,3))
    # I zip two lists above to find the winner
    combine = list(zip(candidate_name, percent_vote))
    # Find the maximum value in a list of percent vote
    for winner,votes in combine:
        if votes == max(percent_vote):
            break
print("Election Results")
print("----------------------")
print(f'Total Votes: {total_voters}')
print("----------------------")

print(f'{candidate_name[0]} : {percent_vote[0]}% ({dict_candidate_value[0]})')
print(f'{candidate_name[1]} : {percent_vote[1]}% ({dict_candidate_value[1]})')
print(f'{candidate_name[2]} : {percent_vote[2]}% ({dict_candidate_value[2]})')
print("----------------------")
print(f'Winner: {winner} ({votes} %)')
print("----------------------")

output = os.path.join('..', 'analysis', 'election_result.txt')
with open(output, 'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-------------------")
    txtfile.write("\n")
    txtfile.write(f'Total Votes: {total_voters}')
    txtfile.write("\n")
    txtfile.write("----------------------")
    txtfile.write("\n")
    txtfile.write(f'{candidate_name[0]} : {percent_vote[0]}% ({dict_candidate_value[0]})')
    txtfile.write("\n")
    txtfile.write(f'{candidate_name[1]} : {percent_vote[1]}% ({dict_candidate_value[1]})')
    txtfile.write("\n")
    txtfile.write(f'{candidate_name[2]} : {percent_vote[2]}% ({dict_candidate_value[2]})')
    txtfile.write("\n")
    txtfile.write("----------------------")
    txtfile.write("\n")
    txtfile.write(f'Winner: {winner} ({votes} %)')
    txtfile.write("\n")
    txtfile.write("----------------------")