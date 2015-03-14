'''
Code for optimizing queries
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 14.03.2015
'''

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
                
    print "Broad Domain Query is\n", broadDomainQuery
    print "Query Specification is\n", querySpecification
    
if __name__ == '__main__':
    initialRequests = 5
    queries = testcases.generateTestCases(initialRequests)
    print len(queries)
    print queries
    broadDomainOptimizer(queries)
    
    
