import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Product_price = []
Product_Description = []
Product_rating = []


for i in range(2,10):   
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY" + str(i)
    r = requests.get(url)   
    soup = BeautifulSoup(r.text, 'html.parser') 

    box = soup.find('div', class_='DOjaWF gdgoEp')

    names = box.find_all('div', class_='KzDlHZ')
    #print(len(names))
    for i in names:
        name = i.text
        Product_name.append(name)
    #print(Product_name)

    prices = box.find_all('div', class_='Nx9bqj _4b5DiR')
    for i in prices:
        price = i.text
        Product_price.append(price)
    #print(Product_price)

    descriptions = box.find_all('ul', class_='G4BRas')
    for i in descriptions:
        description = i.text
        Product_Description.append(description)
    #print(Product_Description)

    ratings = box.find_all('div', class_='XQDdHH')
    for i in ratings:
        rating = i.text
        Product_rating.append(rating)
    #print(len(Product_rating))


df = pd.DataFrame({'Product Name':Product_name, 'Product Price':Product_price, 'Product Description':Product_Description, 'Product Rating':Product_rating})
#print(df)
df.to_csv('Flipkart_Mobiles_under_50000.csv', index=False)



'''
url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)   
'''

'''url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
r = requests.get(url)   
soup = BeautifulSoup(r.text, 'html.parser') 
#print(soup.prettify())'''


'''while True:
    
    np = soup.find('a', class_='_9QVEpD').get('href')
    cnp = "https://www.flipkart.com" + np
    print(cnp)

    url = cnp
    r = requests.get(url)  
    soup = BeautifulSoup(r.text, 'html.parser')'''




