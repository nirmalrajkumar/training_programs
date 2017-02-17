import requests as r
g = r.post('http://122.181.186.42:9200/nirmal', {'name':'nirmal'})
print g.text
