import requests
from bs4 import BeautifulSoup

# Define the URL we want to scrape
url = 'https://www.prisonstudies.org/escape'

# Make a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the prison break information
table = soup.find('table', {'id': 'sortable'})

# Find all rows in the table
rows = table.find_all('tr')

# Loop through each row and extract the relevant information
for row in rows[1:]:  # Skip the header row
    cells = row.find_all('td')
    date = cells[0].text.strip()
    country = cells[1].text.strip()
    prison_name = cells[2].text.strip()
    escapees = cells[3].text.strip()
    details = cells[4].text.strip()
    
    # Do something with the extracted information, like print it
    print(f'{date} - {country} - {prison_name} - {escapees} - {details}')
