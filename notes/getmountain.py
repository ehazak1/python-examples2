'Acquire mountain information and convert it to a convenient form'

import re
import urllib
import BeautifulSoup

url = 'http://www.factmonster.com/ipka/A0001771.html'

def get_min_summit():
    'Named summits over a certain minimum height'
    u = urllib.urlopen(url)
    page = u.read()
    mo = re.search(r'Over ([0-9,]+) Feet', page)
    return int(mo.group(1).replace(',', ''))

def get_mountain_table():
    'Return a list of lists with the parsed Mountain data'
    u = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(u)
    result = []
    t = soup.find('table', id="A0001772")
    for row in t.findAll('tr'):
        result.append([col.text for col in row.findAll('td')])
    return result


def print_fixed_width(rows, colsize):
    colfmt = '{:%d}' % colsize
    for row in rows:
        print ' '.join([colfmt] * len(row)).format(*row)

if __name__ == '__main__':
    from pprint import pprint    

    print get_min_summit()

    table = get_mountain_table()
    print_fixed_width(table, colsize=30)



