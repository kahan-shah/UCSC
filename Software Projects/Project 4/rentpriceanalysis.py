# Kahan Shah
# Rental Price Analysis
# This program is a report generator that takes in an input CSV file containing rental prices in a specific housing market and generates a text file report. 
# Acknowledgements: https://realpython.com/python-csv/, https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/, https://www.geeksforgeeks.org/working-csv-files-python/, and my boi Arin Gadre for quizzing me on the main fuction.



def getRentDetailsFromFile():
    try:
        rowCount=0
        rentList=[]
        #Open input file to read
        with open("sc_rent_prices.csv",'r') as f:
        #Read file
            data = f.read().split('\n')
        #For every line
        for line in data:
            if rowCount!=0:
                row=line.split(",")
                address=row[0]
                neighbourhood=row[1]
                rent2020=(row[2][1:])
                rent2021=(row[3][1:])
                rentList.append([address,neighbourhood,float(rent2020.strip('$')),float(rent2021.strip('$'))])
                rowCount+=1
        return rentList
    except IOError:
        print("Unable to read file.")
    
    
# This gets the average rate of the rent
def getAverageRent2021(rentList):
    sum=0
    for row in rentList:
        sum+=row[3]
    return sum/len(rentList)

# This finds the highest rent of 2021
def getHighestRent2021(rentList):
    highestRent=0
    address=''
    for row in rentList:
        if highestRent<row[3]:
            highestRent=row[3]
            address=row[0]
        return highestRent,address

# This gets the lowest rent of 2021
def getLowestRent2021(rentList):
    lowestRent=rentList[0][3]
    address=''
    for row in rentList:
        if lowestRent>row[3]:
            lowestRent=row[3]
            address=row[0]
    return lowestRent,address

# This shows the average rent change
def getAverageRentChange(rentList):
    sumOfRentChange=0
    for row in rentList:
        rent2020=row[2]
        rent2021=row[3]
        sumOfRentChange+=(rent2020-rent2021)
    return sumOfRentChange/len(rentList)

# This shows the highest rent change
def getHighestRentChange(rentList):
    highestChange=0
    addressOfListing=''
    for row in rentList:
        rent2020=row[2]
        rent2021=row[3]
        rentChange=rent2020-rent2021
    if highestChange<rentChange:
        highestChange=rentChange
        addressOfListing=row[0]
    return highestChange,addressOfListing

# This shows the the smallest rent change
def getLowestRentChange(rentList):
    lowestChange=rentList[0][2]-rentList[0][3]
    addressOfListing=''
    for row in rentList:
        rent2020=row[2]
        rent2021=row[3]
        rentChange=rent2020-rent2021
    if lowestChange>rentChange:
        lowestChange=rentChange
        addressOfListing=row[0]
    return lowestChange,addressOfListing

def getNeighborhoodDictFor2021(rentList):
    neighbourDict={}
    #Add neighbourhood as key and it's rent prices of 2021 as list
    for row in rentList:
        neighbourhood=row[1]
    if neighbourhood in neighbourDict.items():
        rentPriceList=neighbourDict[neighbourhood]
        rentPriceList.append(row[3])
        neighbourDict[neighbourhood]=rentPriceList
    else:
        rentPriceList=[]
        rentPriceList.append(row[3])
        neighbourDict[neighbourhood]=rentPriceList
    return neighbourDict

# This 
def getLeastAffordNeighborhood(rentList):
    neighbourDict=getNeighborhoodDictFor2021(rentList)
    neighbourWithHighestAvgRentPrice=0
    highestAverageRent=0
    for k,v in neighbourDict.items():
        sumOfRent=0
    for rent in v:
        sumOfRent+=rent
        averageRent=sumOfRent/len(v)
    if highestAverageRent<averageRent:
        neighbourWithHighestAvgRentPrice=k
        highestAverageRent=averageRent
    return highestAverageRent,neighbourWithHighestAvgRentPrice

def getMostAffordableNeighborhood(rentList):
    neighbourDict=getNeighborhoodDictFor2021(rentList)
    neighbourWithLowestAvgRentPrice=''
    rowCount=0
    for k,v in neighbourDict.items():
        sumOfRent=0
    for rent in v:
        sumOfRent+=rent
        averageRent=sumOfRent/len(v)
    if rowCount==0:
        lowestAverageRent=averageRent
    if lowestAverageRent>averageRent:
        neighbourWithLowestAvgRentPrice=k
        lowestAverageRent=averageRent
        rowCount+=1
    return lowestAverageRent,neighbourWithLowestAvgRentPrice

# This shows the neghiborhood and the average rent change
def getNeighborhoodAndAverageRentChanges(rentList):
    neighborWithRentChangeList=[]
    neighbourDict={}
    #Add neighbourhood as key and it's change in rent prices as list
    for row in rentList:
        neighbourhood=row[1]
    if neighbourhood in neighbourDict.items():
        rentPriceList=neighbourDict[neighbourhood]
        rentPriceList.append(row[2]-row[3])
        neighbourDict[neighbourhood]=rentPriceList
    else:
        rentPriceList=[]
    rentPriceList.append(row[2]-row[3])
    neighbourDict[neighbourhood]=rentPriceList
    for k,v in neighbourDict.items():
        sumOfRentChanges=0
    for rent in v:
        sumOfRentChanges+=rent
        averageRentChange=sumOfRentChanges/len(v)
        neighborWithRentChangeList.append([k,averageRentChange])
    return neighborWithRentChangeList

# This creates the report
def writeToFile(rentList):
#Open file object
    f = open("report.txt", "w")
    f.write('Rent Report, 2020-2021')
    f.write('\n')
    f.write('Average Rent: $'+str(getAverageRent2021(rentList)))
    f.write('\n')
    highestRent,address=getHighestRent2021(rentList)
    f.write('Highest Rent: $'+str(highestRent)+','+address)
    f.write('\n')
    lowestRent,address=getLowestRent2021(rentList)
    f.write('Lowest Rent: $'+str(lowestRent)+','+address)
    f.write('\n')
    averageRentChange=getAverageRentChange(rentList)
    f.write('Average Rent Change: $'+str(averageRentChange))
    f.write('\n')
    highestRentChange,address=getHighestRentChange(rentList)
    f.write('Highest Rent Change: $'+str(highestRentChange)+','+address)
    f.write('\n')
    lowestRentChange,address=getLowestRentChange(rentList)
    f.write('Lowest Rent Change: $'+str(lowestRentChange)+','+address)
    f.write('\n')
    avgRent,neighborhood=getLeastAffordNeighborhood(rentList)
    f.write('Least Affordable Neighborhood: '+neighborhood+'(Avg Rent:$'+str(avgRent)+')')
    f.write('\n')
    avgRent,neighborhood=getMostAffordableNeighborhood(rentList)
    f.write('Most Affordable Neighborhood: '+neighborhood+'(Avg Rent:$'+str(avgRent)+')')
    f.write('\n')
    f.write('Rent Changes by Neighborhood:\n')
    neighborWithRentChangeList=getNeighborhoodAndAverageRentChanges(rentList)
    for neighbor in neighborWithRentChangeList:
        f.write('\t'+neighbor[0]+'($'+str(neighbor[1])+')')
        f.write('\n')
        f.close()
# Test
def main():
    rentList=getRentDetailsFromFile()
    writeToFile(rentList)
    print('Output file report.txt written successfully')

if __name__ == "__main__":
    main()
