'''
Code for optimizing queries
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 14.03.2015
'''
import time
import testcases

def broadDomainOptimizer(queries):
    '''
    Input : Unoptimized Queries
    Output : Queries optimized through BroadDomain 
    6 Broad Domains including "CSE", "ME", "Meta", "Mining", "EE", "ECE"
    '''
    broadDomainQuery = {}
    querySpecification = {}
    for query in queries : 
        if query['interest'] is None:
            querySpecification[query['queryId']] = []
            continue
        for interest in query['interest']:
            try:
                broadDomainQuery[interest['broadDomain']].add(query['queryId'])
            except KeyError:
                broadDomainQuery[interest['broadDomain']] = set([query['queryId']])
            try: 
                if interest['broadDomain'] not in querySpecification[query['queryId']]:
                    querySpecification[query['queryId']].append(interest['broadDomain'])
            except KeyError:
                querySpecification[query['queryId']] = [interest['broadDomain']]
                
    #~ print "Broad Domain Query is\n", broadDomainQuery
    #~ print "Query Specification is\n", querySpecification
    #~ 
    return querySpecification, len(broadDomainQuery)
    
def CFPOptimizer(queries):
    '''
    Input : Unoptimized Queries
    Output : Queries optimized through CFP
    Maximum CFP till next one year
    '''
    CFPQuery = {}
    querySpecification = {}
    for query in queries :
        if query['cfpDate'] is None:
            querySpecification[query['queryId']] = None
        else: 
            currMonth = time.strftime("%m")
            cfpMonth = int(query['cfpDate'].split("-")[1])-int(currMonth)
            if cfpMonth < 0 : 
                cfpMonth += 12
            querySpecification[query['queryId']] = cfpMonth
            try :
                CFPQuery[cfpMonth].append(query['queryId'])
            except KeyError :
                CFPQuery[cfpMonth] = [query['queryId']]
    
    #~ print "Broad CFP Query is\n", CFPQuery
    #~ print "Query Specification is\n", querySpecification
    #~ 
    return querySpecification, len(CFPQuery)


def LocationOptimizer(queries):
    '''
    Input : Unoptimized Queries
    Output : Queries optimized through Location States
    '''
    locationQuery = {}
    querySpecification = {}
    for query in queries : 
        if query['location'] is None:
            querySpecification[query['queryId']] = []
            continue
        for location in query['location']:
            try:
                locationQuery[location['state']].add(query['queryId'])
            except KeyError:
                locationQuery[location['state']] = set([query['queryId']])
            try: 
                if location['state'] not in querySpecification[query['queryId']]:
                    querySpecification[query['queryId']].append(location['state'])
            except KeyError:
                querySpecification[query['queryId']] = [location['state']]
                
    #~ print "location Query is\n", locationQuery
    #~ print "Query Specification is\n", querySpecification
    #~ 
    return querySpecification, len(locationQuery)
    
def finalResults(list1, list2):
    '''
    given list1 and list2 gives list3 which is the intersection of two 
    lists
    Input : list1 and list2 which will have conference id's from 2 
            different queries
    Output : list3 comprises of intersection of conference id's which 
            are the intersection of the list1 id's and list2 id's
    '''
    return [val for val in list1 if val in list2]

#~ if __name__ == '__main__':
    initialRequests = 2
    optimizedQueries = {}
    queries = testcases.generateTestCases(initialRequests)
    queryBroadOpt, totalQuery = broadDomainOptimizer(queries)
    for query in queryBroadOpt:
        optimizedQueries[query] = {"BroadDomain":queryBroadOpt[query]}
    queryCFPOpt,CFPQuery = CFPOptimizer(queries)
    totalQuery += CFPQuery
    for query in queryCFPOpt:
        optimizedQueries[query]["CFPDate"] = queryCFPOpt[query]
    queryState, locationQuery = LocationOptimizer(queries)
    totalQuery += locationQuery
    for query in queryState:
        optimizedQueries[query]["State"] = queryState[query]
    #~ print "Total number of Queries", len(queries)
    #~ print "Optimized Queries", totalQuery
    print optimizedQueries
    #~ print finalResults([1,2,4,3,5],[1,3,5,6,35,12,4])
