'''
Code for finding related conferences
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 22.03.2015
'''

def relatedConf(interest, state, publisher):
    '''
    interest : tuple of (broadDomain, specificDomain)
    state : State in which a given conference will be taking place
    publisher : Publisher of a given conference
    '''
    ## Form a get request with sponsorship = 1
    ## sponsList will have list of confId's which satisfy above criteria
    sponsList = {}
    ## Form a get request with given publisher
    ## pubList will have list of confId's which satisfy above criteria
    pubList = {}
    for indInterest in interest :
        ## Form a get request with (broadDomain, specificDomain) 
        ## domainList will have list of confId's which satisfy above criteria
        domainList = {}
    ## Form a get request with given state 
    ## stateList will have list of confId's which satisfy above criteria
    stateList = {}
    semiRelatedConference = finalResults(pubList, stateList)
    relatedConference = finalResults(semiRelatedConference, domainList)
    if len(sponsList) != 0 : 
        relatedConference  = finalResults(sponsList, relatedConference)
        if len(relatedConference) == 0:
            relatedConference = finalResults(semiRelatedConference, sponsList)
        if len(relatedConference) == 0:
            relatedConference = finalResults(domainList, sponsList)
        if len(relatedConference) == 0:
            relatedConference = finalResults(pubList, sponsList)
    if len(relatedConference) == 0:
        relatedConference = semiRelatedConference
    if len(relatedConference) == 0:
        relatedConference = domainList
    if len(relatedConference) == 0:
        relatedConference = pubList
    return relatedConference
    
def finalResults(list1, list2):
    '''
    given list1 and list2 gives list3 which is the intersection of two 
    lists . Will be done for the output recieved
    Input : list1 and list2 which will have conference id's from 2 
            different queries
    Output : list3 comprises of intersection of conference id's which 
            are the intersection of the list1 id's and list2 id's
    '''
    return [val for val in list1 if val in list2]
    
def getConfDetails(confId):
    '''
    Give confId get details about a conference
    Write Get Request here
    Connect it with relatedConf
    '''
    
if __name__ == '__main__':
    #~ getConfDetails(id)
    
