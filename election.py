import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

if __name__ == "__main__":
    url = 'https://results.eci.gov.in/pc/en/partywise/index.htm'
    website_url = requests.get(url).text
    soup = BeautifulSoup(website_url,'lxml')
    table = soup.find('table', {'class': 'table-party'})
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
    output_rows = sorted([i for i in output_rows[:-2] if len(i) > 2], key=lambda i:int(i[2]), reverse=True)+output_rows[-2:]
    print(tabulate(output_rows, headers= ['PARTY', 'WON', 'LEADING', 'TOTAL']))
