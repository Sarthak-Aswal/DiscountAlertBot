import lxml
import requests
from bs4 import BeautifulSoup


# scrapes the amazon website and get the current price of the desired product
def getCurrentPrice(url, userAgent):
    response = requests.get(url, headers={'User-Agent': userAgent}) # making https request
    print(response)
    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, 'lxml')  # creating a soup object
        price = soup.find('span', class_="a-price-whole").text.replace(',', '')
        price = float(price)
        return price
    else:
        return -1


# gets the original price of product from a file that stores the original price
def getOriginalPrice():
    with open('originalPrice.txt', 'r') as p:
        originalPrice = float(p.read())
    return originalPrice


# sets the original price of the product  in a file called originalPrice.txt.It will run only 1 time at the starting
def setPrice(currentPrice):
    with open('originalPrice.txt', 'w') as p:
        p.write(currentPrice)
