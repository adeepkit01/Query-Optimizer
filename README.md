# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
	userId:
	beginDate:
	endDate: 
	// Date format would be same as `date +"%d-%m-%Y"`
	location:[{
			state:
			,city:
		},{}]
	interest:[{
			broadDomain:
			,specificDomain:
			},{}]	
	affilifation:[]
	lowestRank:
	highestRank: 
}
```
For all those places where nothing is there just add `null` or `None` (in python) to it. <br>
