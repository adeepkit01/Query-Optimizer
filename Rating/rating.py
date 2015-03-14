'''
Code for optimizing queries
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 14.03.2015
'''

def ratingGen(flagship, affiliation, featured, 
                qualityCollege, indexing, numberOfPrev, userExp):
    '''
    Generates rating 0(min) to 5(max) given a conference parameters
    
    Input : conferenceId but taken different parameters for easy testing
    
    flagship : Boolean Variable whether a conference is flagship or not
    affiliation : Bool variable whether conference is affiliated to some
                  publishing house like IEEE, Springer etc
    featured : float variable [0-1 (both included)] decided on the basis
                of relative sponsorship provided
    qualityCollege : Quality of college integer depending on tier
                    based on tiers provided by government
    indexing : Bool variable whether it is dblp indexed or not 
    numberOfPrev : Number of previous conferences under the same hood 
                    integer value
    userExp : None or float [0-1 (both included)] depending whether it 
            is an old conference or new
    
    Output : A rating of the conference
    '''
    netRank = 0.5
    if flagship == 1 :
        netRank += 0.5
    if affiliation == 1:
        netRank += 0.5
    netRank += featured
    if numberOfPrev > 0 and numberOfPrev < 5:
        netRank += 0.2
    elif numberOfPrev < 10 :
        netRank += 0.35
    elif numberOfPrev > 10: 
        netRank += 0.5
    if qualityCollege == 1 :
        netRank += 0.5
    if qualityCollege == 2 :
        netRank += 0.2
    if indexing == 1: 
        netRank += 0.5
    netRank += userExp
    return netRank
    
if __name__ == '__main__':
    print ratingGen(1,1,1,1,1,100,1)
