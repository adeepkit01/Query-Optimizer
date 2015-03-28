'''
Analytics Generation Email
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 28.03.2015
Install cairoplot using http://cairoplot.sourceforge.net/tutorials.html
'''
#!/usr/bin/env python

import cairoplot

def catalogEntry(confId): 
    '''
    confId : A conference Id
    A graph of last week catalog entry
    '''
    listOfVisits = [1,2,3,4,2,3,2,14,2,2,422,4,2,2,14,1,41,41,24,42,41,41]
    # Get list of visits from an API
    cairoplot.dot_line_plot('catalogEntry.png', listOfVisits[-7:], 1000, 700, axis=True, dots=True, border = 50, x_title="Number of days", y_title="Number of Visits",series_colors =[(1.0,0.0,0.0)])

def numberOfVisit(confId): 
    '''
    confId : A conference Id
    A graph of last week page visit
    '''
    listOfVisits = [1,2,3,4,2,3,2,14,2,2,422,4,2,2,14,1,41,41,24,42,41,41]
    # Get list of visits from an API
    cairoplot.dot_line_plot('weekVisit.png', listOfVisits[-7:], 1000, 700, axis=True, dots=True, border = 50, x_title="Number of days", y_title="Number of Visits",series_colors =[(1.0,0.0,0.0)])

def websiteVisit(confId): 
    '''
    confId : A conference Id
    A graph of last week website visit
    '''
    listOfVisits = [1,2,3,4,2,3,2,14,2,2,422,4,2,2,14,1,41,41,24,42,41,41]
    # Get list of visits from an API
    cairoplot.dot_line_plot('weekVisit.png', listOfVisits[-7:], 1000, 700, axis=True, dots=True, border = 50, x_title="Number of days", y_title="Number of Visits",series_colors =[(1.0,0.0,0.0)])
    
if __name__ == '__main__':
    numberOfVisit(1)
