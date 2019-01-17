from decimal import Decimal
from pprint import pprint
import requests
import feedparser

today = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26')
tommorow = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26&Day=tomorrow')

feedtoday = feedparser.parse(today.content)
todaylist = feedtoday['entries']
for i in todaylist :
    i['day'] = ''
    
feedtommorow = feedparser.parse(tommorow.content)
tommorowlist = feedtommorow['entries']
for i in tommorowlist :
    i['day'] = 'style="background-color:#ff0000;"'

feedAll = todaylist + tommorowlist

def by_price(item):
    return item['price']

sorted_feedAll=sorted(feedAll, key=by_price)

for i in range(len(sorted_feedAll)):

    print('Suburb: '+ sorted_feedAll[i]['location'] + '  Price:'+sorted_feedAll[i]['price'] + '  Brand:'+sorted_feedAll[i]['brand'])



f = open('table.html', 'w')
rows = ''
for i in sorted_feedAll:
    
    rows += """
    
    <tr {day}>\n
        <td>{loc}</td>\n<td>{price}</td>\n<td>{brand}</td>\n
        </tr>\n
       
    """.format(loc=i['location'], price=Decimal(i['price'])/100,brand = i['brand'],day = i['day'])


head = """
        <table>
    <thead>
        <tr>
            <th>Suburb</th>
          	<th>Fuel Price/$</th>
          	<th>Fuel Station</th>
        </tr>
    </thead>

<tbody>\n
"""
tail = ' </tbody>\n</table>\n'
f.write(head + rows + tail)
f.close()
