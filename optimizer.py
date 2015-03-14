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
    return querySpecification
    
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
    return querySpecification

if __name__ == '__main__':
    initialRequests = 2
    optimizedQueries = {}
    queries = testcases.generateTestCases(initialRequests)
    print len(queries)
    queryBroadOpt = broadDomainOptimizer(queries)
    for query in queryBroadOpt:
        optimizedQueries[query] = {"BroadDomain":queryBroadOpt[query]}
    queryCFPOpt = CFPOptimizer(queries)
    for query in queryCFPOpt:
        optimizedQueries[query]["CFPDate"] = queryCFPOpt[query]
    print optimizedQueries
