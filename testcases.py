'''
Test Cases Generation Code
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 08.02.2015
'''

from random import randint, choice

def generateTestCases(numberOfUsers, minNumberOfQueries, maxNumberOfQueries):
    '''
    Returns the JSON object with queries
    Args:
        numberOfUsers : Number of users querying the system
        minNumberOfQueries : JSON should have minimum this much number of queries 
        maxNumberOfQueries : JSON should have maximum this much number of queries 
    Returns:
        outputQuery : JSON object
    '''
    ## Assuming userId is maximum number of 7 digits.
    outputQuery = []
    for user in xrange(numberOfUsers):
        tempQuery = {}
 
        userId = random.randint(1, 10000000)
 
        tempQuery["userId"] = userId
        beginDay = randint(1, 27)
        beginMonth = randint(1, 12)
        beginYear = randint(2015, 2020)
        beginDate = str(beginDay + "-" + beginMonth + "-"+ beginYear)
        endDate = str(randint(beginDay+1,28)+"-"+randint(beginMonth,12)
                        +"-"+randint(beginYear,2025))
        tempQuery["beginDate"] = beginDate
        tempQuery["endDate"] = endDate
 
        affiliation = []
        affiliationNumber = random.randint(1,3)
        if i == 3 : 
            affiliation = ["IEEE", "ACM" , "Springer"]
        elif i==2 : 
            affiliation = random.choice([["IEEE","ACM"],
                            ["Springer","ACM"],["IEEE","Springer"]])
        else : 
            affiliation = random.choice(["Springer","IEEE","ACM"])
        tempQuery["affiliation"] = affiliation
        
        tempQuery["lowestRank"] = random.uniform(1,5)
        tempQuery["highestRank"] = random.uniform(
                        tempQuery["lowestRank"] + 0.001, 5)
                    
        location = []
        states = [Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhatisgarh, Goa,
        Gujarat, Haryana , Himachal Pradesh, Jammu & Kashmir, Jharkhand, Karnataka,
        Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland,
        Orissa, Punjab, Rajasthan, Sikkim, Tamil Nadu, Tripura, Uttar Pradesh,
        Uttaranchal, West Bengal]
        cities = []
        numberOfLocations = random.randInt(1,28)
        for states in xrange(numberOfLocations):
            location.append({"state":states[random.randint(0,28)],
                            "city": None })
        tempQuery["location"] = location
        
        interest = []
        broadDomain = ["CSE", "ME", "Meta", "Mining", "EE", "ECE", "IT"]
        mapSpec = {}
        mapSpec["specificDomainCSE"] = ["Networks", "AI", "ML", "SE", "IS"]
        mapSpec["specificDomainME"] = ["Robotics", "Workshop", "Lathe"]
        mapSpec["specificDomainMeta"] = ["Soil", "Temperature" , "Rock"]
        mapSpec["specificDomainMining"] = ["Soil", "Temperature"]
        mapSpec["specificDomainEE"] = ["Signal", "Image" , "Transistor", "Power"]
        mapSpec["specificDomainECE"] = ["Signal", "Image" , "Transistor"]
        mapSpec["specificDomainIT"] = ["Networks", "AI", "ML", "SE", "IS"]
        numberOfInterest = random.randint(1,5)
        for domain in xrange(numberOfInterest):
            interestSpec = random.randint(0,6)
            numberOfSpec = random.randint(1,3)
            for specification in xrange(numberOfSpec):
                interest.append({"broadDomain": broadDomain[interestSpec]
                , "specificDomain": 
                mapSpec[str(specificDomain)+str(broadDomain[interestSpec])]
                [random.randint(0,2)]})
        tempQuery["interest"] = interest
        
        outputQuery.append(tempQuery)
        
if __name__ == '__main__':
    generateTestCases(3, 1, 4)
