from bs4 import BeautifulSoup
html = """
soup = BeautifulSoup('http://26.0.12.33','html5lib')
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.body)

for link in soup.find_all('a'):
     print(link.get('href'))

print(soup.get_text())
