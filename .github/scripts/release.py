#!/usr/bin/env python
import os
from bs4 import BeautifulSoup
className = os.environ.get('CLASS_NAME')
tableData = os.environ.get('NEW_TABLE')
with open('.github/workflows/release-notes.html', 'r') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
new_soup = BeautifulSoup(tableData, 'html.parser')
srs = soup.find('div', {'class': className})
if srs is None:
    print('not present')
    with open('.github/workflows/release-notes.html', 'a') as f:
        f.write(tableData)
else:
    print('present')
    srs.contents = new_soup.div.contents
    with open(".github/workflows/release-notes.html", "w") as f:
        print(soup)
        f.write(str(soup))