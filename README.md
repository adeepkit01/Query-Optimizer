# Query-Optimizer<br>
Query format will be as follows : <br>
```
{
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
Each query object will be of form <br> `userId:[query1,query2,..]`<br>
and the QueryOptimizer object will take an array of query objects as<br>
input and return <br>
`userId1:[result1,result2,..],userId2:[result1,result2,..]`<br>
