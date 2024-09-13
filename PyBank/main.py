#assignment 1 breze howard

#importing os and csv file 
import os
import csv

#variable
keep_going = 'y'

#collects everything 
def main():
    data = getdata()
    total = totalChangeFunction(data)
    getfile()
    months(data)
    totalamount(data)
    totalChangeFunction(data)
    greatestprofitincrease(data, total)
    biggestprofitdecrease(data, total)

#getting budget data
def getdata():
    with open("PyBank/resources/budget_data.csv", "r") as sales: 
        get = csv.reader(sales)
        next(get)
        data = []
        for dates in get:
            data.append(dates)
    return data

#writing analysis to txt file   
def getfile():
    newfile = open("PyBank/Analysis/Analysis.txt","w")
    newfile.writelines(f"Financial Analysis\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    newfile.close()
    return newfile

#getting total months
def months(data):
    totalmonths = len(data)
    print(f"Months: {totalmonths}")
    newfile = open("PyBank/Analysis/Analysis.txt","a").writelines(f"Months: {totalmonths}\n")

#getting total amount
def totalamount(data):
    amount = []
    for dates, values in data:
        amount.append(int(values))
        netamount = sum(amount)
    print(f"Net Amount: {netamount}")
    open("PyBank/Analysis/Analysis.txt","a").writelines(f"Net Amount: {netamount}\n")

#getting change total
def totalChangeFunction(data):
    total = []
    for values in range(1,len(data)):
        changes = int(data[values][1]) - int(data[values-1][1])
        total.append(changes)
    return total

#getting average 
def average(data, total):
    if total:
        average = sum(total)/len(total)
    else:
        average = 0
    print(f"Average Change: {average:.2f}") 
    open("PyBank/Analysis/Analysis.txt","a").writelines(f"Average Change: {average:.2f}\n")

#getting biggest profit increase
def greatestprofitincrease(data, total):
    increase = max(total) 
    index = total.index(increase) + 1
    Increasedate = data[index][0] 
    print(f"Greatest Increase in Profits: {Increasedate}({increase})")
    open("PyBank/Analysis/Analysis.txt","a").writelines(f"Greatest Increase in Profits: {Increasedate}({increase})\n")

#getting biggest profit decrease
def biggestprofitdecrease(data, total): 
    decrease = min(total) 
    index = total.index(decrease) + 1
    decreasedate = data[index][0]
    print(f"Biggest Profit Decrease: {decreasedate}({decrease})")
    newFile = open("PyBank/Analysis/Analysis.txt","a").writelines(f"Biggest Profit Decrease: {decreasedate}({decrease})\n")

#call the function and restart
while keep_going == 'y':
    main()
    keep_going = input ('would you like to run again? ')