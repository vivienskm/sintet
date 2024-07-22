from bs4 import BeautifulSoup

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Convert the soup object to a string
soup_string = str(soup)
