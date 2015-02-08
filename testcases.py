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
    ## Assuming userId is numerical of 6 digits.
    outputQuery = []
    for user in xrange(numberOfUsers):
        tempQuery = {}
 
        userId = random.randint(1, 1000000)
 
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
                    
        ## Location and Interest Remaining
        
if __name__ == '__main__':
    generateTestCases(3, 1, 4)
