from requests import get
from pprint import pprint
from bs4 import BeautifulSoup
import re

## Make a request to "http://18.207.92.139:8000/random_company"
resp = get("http://18.207.92.139:8000/random_company")
resp.text
pprint(resp.text)

## Extract the name and purpose of the generated company.
soup=BeautifulSoup(resp.text,'html.parser')
name=soup.find(text=re.compile('Name'))
purpose=soup.find(text=re.compile('Purpose'))
pprint(name)
pprint(purpose)


## put it all together
## Repeat this 50 times 
def main():
    name_purpose = open("name_purpose.txt", 'w')
    for i in range(50):
        resp = get("http://18.207.92.139:8000/random_company")
        
        soup=BeautifulSoup(resp.text,'html.parser')
        name=soup.find(text=re.compile('Name'))
        purpose=soup.find(text=re.compile('Purpose'))
        
        pprint(name)
        pprint(purpose)
        
    name_purpose.close()

if __name__ =='__main__':
    main()
