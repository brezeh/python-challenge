#assignment 1 breze howard

#importing os and csv file 
import os
import csv

#variable
keep_going = 'y'

#collects everything 
def main():
    getfile()
    data = getdata()
    total = votetotal(data)
    candidates = candidatelist(data)
    percent(data, total, candidates)

#getting elrection data
def getdata():
    with open("PyPoll/Resouces/election_data.csv", "r") as results:
        get = csv.reader(results)
        next(get)
        data = []
        for dates in get:
            data.append(dates)
    return data

#writing analysis to txt file   
def getfile():
    newfile = open("PyPoll/Analysis/Analysis.txt","w")
    newfile.writelines(f"Election Analysis\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    newfile.close()
    return newfile

#getting total amount of votes
def votetotal(data):
    total = len(data)
    print(f"Election Results\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nTotal Votes: {total}\n")
    newfile = open("PyPoll/Analysis/Analysis.txt", "a").writelines(f"Total Votes: {total}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    return total

#getting list of canidates
def candidatelist(data):
    candidates = [] 
    for values in data: 
        candidate = values[2] 
        if candidate not in candidates: 
            candidates.append(candidate)
    return candidates

#getting percentage of votes for the top 3 canidates 
def percent(data, total, candidates):
    topcanidates = {}
    counts = {candidate: 0 for candidate in candidates} 
    for values in data:
        candidates = values[2]
        counts[candidates] += 1 
    for candidate, votes in counts.items(): 
        percentage = (votes/total)*100 
        topcanidates.update({candidate:percentage})
        print(f"{candidate}: {percentage:.4f}% ({votes})\n")
        newfile = open("PyPoll/Analysis/Analysis.txt", "a").writelines(f"{candidate}: {percentage:.4f}% ({votes})\n")
    winner = max(zip(topcanidates.values(), topcanidates.keys()))[1]
    print(f"the winner is: {winner}")   
    newfile = open("PyPoll/Analysis/Analysis.txt", "a").writelines(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n the winner is: {winner}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#call the function and restart
while keep_going == 'y':
    main()
    keep_going = input ('would you like to run again? ')