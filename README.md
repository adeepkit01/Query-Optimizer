# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
	userId:
	queryId:
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
	{
		'publisher': None, 
		'endDate': '13-12-2024', 
		'interest': 
			[{'specificDomain': 'Temperature', 'broadDomain': 'Meta'}, 
			{'specificDomain': 'Soil', 'broadDomain': 'Meta'}], 
		'lowestRank': 1.3407697776717198, 
		'beginDate': '11-9-2017', 
		'userId': 5765005, 
		'queryId': 3015209, 
		'location': None, 
		'cfpDate': '11-9-2017', 
		'highestRank': 6
	}
]

```
