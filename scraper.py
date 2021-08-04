import requests
from bs4 import BeautifulSoup
import smtplib
import time

# The webpage URL
URL = "https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?crid=4V1IK8W6ESN5&dchild=1&keywords=sony+a7iii&qid=1628061492&sprefix=sony%2Caps%2C312&sr=8-3"

# Headers for request
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 'Accept-Language': 'en-US, en; q=0.5'})

def check_price():
    # HTTP Request
    page = requests.get(URL, headers=HEADERS)

    # Soup object containing all data
    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:-3].replace(',',''))

    if (converted_price < 1700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('taraasik@gmail.com', 'eyomymdwubalwdvg')
    
    subject = 'Price fell down!'
    
    body = 'Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?crid=4V1IK8W6ESN5&dchild=1&keywords=sony+a7iii&qid=1628061492&sprefix=sony%2Caps%2C312&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'taraasik@gmail.com',
        'taraasik@gmail.com',
        msg
    )
    
    print('HEY EMAIL HAS BEEN SENT!')
    
    server.quit()
    
while(True):
    check_price()
    time.sleep(86400) #check the price every day