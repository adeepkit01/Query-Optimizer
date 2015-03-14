# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
	userId:
	beginDate:
	endDate: 
	cfpDate: 
	// Last date of paper submission
	// Date format would be same as `date +"%d-%m-%Y"`
	location:[{
			  country:
			, state:
			, city:
		},{}]
	interest:[{
			broadDomain:
			,specificDomain:
			},{}]	
	publisher:[]
	lowestRank:
	highestRank: 
}
```
For all those places where nothing is there just add `null` or `None` (in python) to it. <br>

###Sample Query :

```
[
	{'publisher': None,
	 'endDate': '26-10-2021', 
	 'cfpDate': '9-1-2015',
	 'lowestRank': 3.550249160539083,
	 'beginDate': '9-1-2015', 
	 'userId': 1914880, 
	 'location': None, 
	 'interest': 
		[{'specificDomain': 'Signal', 'broadDomain': 'EE'}, 
		{'specificDomain': 'Signal', 'broadDomain': 'EE'}], 
	 'highestRank': 3.552828898086108
	}
]

```
