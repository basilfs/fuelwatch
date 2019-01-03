from pprint import pprint
import requests
import feedparser

today = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26')
tommorow = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26&Day=tomorrow')

feedtoday = feedparser.parse(today.content)
feedtommorow = feedparser.parse(tommorow.content)


##pprint(feed, indent=4)

##pprint(type(feed))

todaylist = feedtoday['entries']
tommorowlist = feedtommorow['entries']
feedAll = todaylist + tommorowlist

def by_price(item):
    return item['price']

sorted_feedAll=sorted(feedAll, key=by_price)

for i in range(len(sorted_feedAll)):
    print('<tr>')
    print('')
    print('Suburb: '+ sorted_feedAll[i]['location'] + '  Price:'+sorted_feedAll[i]['price'] + '  Brand:'+sorted_feedAll[i]['brand'])



f = open('table.html', 'w')
f.write("""
        <table>
    <thead>
        <tr>
            <th>Suburb</th>
          	<th>Fuel Price</th>
          	<th>Fuel Station</th>
        </tr>
    </thead>
""")
f.write('<tbody>\n')
for i in range(len(sorted_feedAll)):
   
    f.write('<tr>\n')
    f.write('<td>'+ sorted_feedAll[i]['location']+'</td>\n''<td> '+sorted_feedAll[i]['price']+'</td>\n''<td>'+sorted_feedAll[i]['brand']+'</td>\n')
    f.write('</tr>\n')
f.write('</tbody>\n')
f.write('</table>\n')




f.close()
