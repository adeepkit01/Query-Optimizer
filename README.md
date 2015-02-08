# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
	beginDate:
	endDate: 
	// Date format would be same as `date +"%d-%m-%Y"`
	location:[{
			state:
			city:
		},{}]
	interest:[{
			broadDomain:
			specificDomain:[specifcDomain1,specificDomain2]
			},{}]	
	affilifation:[]
	lowestRank:
	highestRank: 
}
```
For all those places where nothing is there just add `null` to it. <br>
