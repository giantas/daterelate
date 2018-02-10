# DateRelate

Relate two dates to each other easily (e.g. today to tomorrow, new year to today)

# Usage
```
$ pip install daterelate
```

+ Relate using datetime objects
```python
>>> from daterelate.daterelate import relate
>>> from datetime import datetime
>>>
>>> tomorrow  = datetime.strptime('12-12-2017', '%d-%m-%Y')
>>> next_occurrence = datetime.strptime('2-02-2018', '%d-%m-%Y')
>>>
>>> relate(next_occurrence, tomorrow)	# relate next_occurrence to tomorrow
'52 days to come'
>>>
>>> relate(next_occurrence, tomorrow, future='remaining')
'52 days remaining'
```

+ Relate using string values
```python
>>> from daterelate.daterelate import relate_from_string
>>>
>>> tomorrow  = datetime.strptime('12-12-2017', '%d-%m-%Y')
>>> next_occurrence = datetime.strptime('2-02-2018', '%d-%m-%Y')
>>>
>>> relate_from_string('12/12/2017')	# relate next_occurrence to current date, return value depends on current date
>>>
>>> relate_from_string('12/12/2017', '2/02/2018', future='before the eclipse')
'52 days before the eclipse'
```

# More
... to be added

# etc
Distributed under [MIT](LICENSE)
