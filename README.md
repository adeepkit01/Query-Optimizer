# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
	userId:
	beginDate:
	endDate: 
	// Date format would be same as `date +"%d-%m-%Y"`
	cff: 
	// Last date of paper submission
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
	flagship: 
	// Bool variable
}
```
For all those places where nothing is there just add `null` or `None` (in python) to it. <br>
