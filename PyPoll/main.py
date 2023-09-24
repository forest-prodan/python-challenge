import os
import csv

#assign path to data file
poll_csv = os.path.join("Resources", "election_data.csv")

#create lists to store data
candidate = []

#cast variables
cand_per_1 = 0
cand_per_2 = 0
cand_per_3 = 0
cand_1 = str("Charles Casper Stockham")
cand_votes_1 = 0
cand_2 = str("Diana DeGette")
cand_votes_2 = 0
cand_3 = str("Raymon Anthony Doane")
cand_votes_3 = 0
cand_winner = str()

#open and read data file
with open(poll_csv) as csvfile:
    poll_open = csv.reader(csvfile)
    
    #skip header row
    csvheader = next(csvfile)
    
    #assign necessary column to list 
    for row in poll_open:
        candidate.append(row[2])
    
    #count rows to determine total votes
    tot_votes = int(len(candidate))

    #loop through data and add to vote counts
    for i in range(len(candidate)):
        if candidate[i] == cand_1:
        		cand_votes_1 = cand_votes_1 + 1
        elif candidate[i] == cand_2:
        		cand_votes_2 = cand_votes_2 + 1
        elif candidate[i] == cand_3:
        		cand_votes_3 = cand_votes_3 + 1

#calculate percentage totals                
cand_per_1 = cand_votes_1 / tot_votes
cand_per_2 = cand_votes_2 / tot_votes
cand_per_3 = cand_votes_3 / tot_votes

#compare vote counts to determine winners
if cand_votes_1 > cand_votes_2 and cand_votes_1 > cand_votes_2:
    cand_winner = cand_1
if cand_votes_2 > cand_votes_1 and cand_votes_2 > cand_votes_3:
    cand_winner = cand_2
if cand_votes_3 > cand_votes_1 and cand_votes_3 > cand_votes_2:
    cand_winner = cand_3

#print results as shown                
print(f"Election Results")
print(f"---------------------") 
print(f"Total Votes: {tot_votes}")
print(f"---------------------")
print(f"{cand_1}: {round((cand_per_1*100), 3)}% ({cand_votes_1})")
print(f"{cand_2}: {round((cand_per_2*100), 3)}% ({cand_votes_2})")
print(f"{cand_3}: {round((cand_per_3*100), 3)}% ({cand_votes_3})")               
print(f"---------------------")
print(f"Winner: {cand_winner}")
print(f"---------------------")

#open analysis file and write results    
poll_file = os.path.join("analysis", "poll_analysis.txt")
with open (poll_file, "w") as analysis:
    analysis.write(f"Election Results\n")
    analysis.write(f"---------------------\n")
    analysis.write("Total Votes: {tot_votes}\n")
    analysis.write(f"---------------------\n")
    analysis.write(f"{cand_1}: {round((cand_per_1*100), 3)}% ({cand_votes_1})\n")
    analysis.write(f"{cand_2}: {round((cand_per_2*100), 3)}% ({cand_votes_2})\n")
    analysis.write(f"{cand_3}: {round((cand_per_3*100), 3)}% ({cand_votes_3})\n")               
    analysis.write(f"---------------------\n")
    analysis.write(f"Winner: {cand_winner}\n")
    analysis.write(f"---------------------\n")