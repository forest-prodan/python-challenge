#this is the file for bank

#get that file in there
import os
import csv

bank_csv = os.path.join("Resources","budget_data.csv")

#create list to store each collumn's data
date = []
pl = []   
data = []

#cast numerical variables
tot = 0 
value = 0
line = 0
line1 = 0
value1 = 0
change_tot = 0
price_change = 0

#open the file
with open(bank_csv) as csvfile:
    
    #read the file
    bank_open = csv.reader(csvfile)
    
    #skip the header row
    csvheader = next(csvfile)
    
    #assign collumns to lists
    for row in bank_open:
        date.append(row[0])
        pl.append(row[1])
        data.append(row)
        
        #convert list data to integer for math functions
        pl=[int(j) for j in pl]
        
        
    #count the rows to determine the number of months
    months = int(len(date))
    
    #determine the sum of the Profit/Losses collumn
    tot = int(sum(pl))
    
    #loop through list containing all the data
    for i in range(len(data)):
        #current row as today
        todays_row = data[i]
        #todays date as first collumn value
        todays_date =  todays_row[0]
        #todays price as second collumn value
        todays_price = int(todays_row[1])
        #previous row as yesterdat
        yesterdays_row = data[i-1]
        #yesterdays price as previous row second collumn value
        yesterdays_price = int(yesterdays_row[1])
        #omit the first row as there is no previous days price
        if i != 0:
            #calculate change in price
            price_change = (todays_price - yesterdays_price)
            #add change in price to total change counter
            change_tot = change_tot + (price_change)
      
        
    
     
        #if change in price is greater than previous stored value
        if price_change>value:
            #store the price change
            value = price_change
            #store row value for highest increase 
            line = i
        #if change is not greater than previously stored
        else:
            #don't change stored price chane
            value=value
        #if change in price is less than previously stored value    
        if price_change<value1:
            #store the price change
            value1 = price_change
            #store row value for highest decrease
            line1 = i
        #if change is not lower than previously stored
        else:
            #don't change the stored value
            value1=value1

#calculate average change (makes round function easier)
avg_change = change_tot/(months - 1)
        
print(f'Financial Analysis')
print(f'-------------------------------------------')   
print(f"Total Months: {months}")    
print(f"Total: ${tot}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {date[line]} (${value})")
print(f"Greatest Decrease in Profits: {date[line1]} (${value1})")

budget_file = os.path.join("analysis","bank_analysis.txt")
with open (budget_file, "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write(f'-------------------------------------------\n') 
    analysis.write(f"Total Months: {months}\n")
    analysis.write(f"Total: ${tot}\n")
    analysis.write(f"Average Change: ${round(avg_change,2)}\n")
    analysis.write(f"Greatest Increase in Profits: {date[line]} (${value})\n")
    analysis.write(f"Greatest Decrease in Profits: {date[line1]} (${value1})\n")
    
    
      
            
        
    
        