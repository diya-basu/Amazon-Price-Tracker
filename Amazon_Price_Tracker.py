import requests
from bs4 import BeautifulSoup
import html
import smtplib 


currency_symbols = ['€', '  £', '$', "¥", "HK$", "₹", "¥", "," ] 

url="https://www.amazon.in/Apple-iPad-Air-10-9-inch-27-69-Wi-Fi/dp/B09V4FNFHN/ref=sr_1_3?crid=1XLPC6U49JO9T&keywords=ipad&qid=1684663247&sprefix=ipad%2Caps%2C446&sr=8-3&th=1"
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Lanuage":"en-US,en;q=0.9",
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
}

response=requests.get(url,headers=header)
soup=BeautifulSoup(response.content, "html.parser")
product_title = soup.find('span', class_ = "a-size-large product-title-word-break").getText()
product_price = soup.find('span', class_ = "a-offscreen").getText()

for i in currency_symbols : 
        product_price = product_price.replace(i,'')

ProductTitleStrip = product_title.strip()
ProductPriceStrip = product_price.strip()
print(ProductTitleStrip)
print(ProductPriceStrip)



buyprice="55000.00"
title=soup.find_all()

if ProductPriceStrip<buyprice:
    message=f"{ProductTitleStrip}is now {ProductPriceStrip}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("diya.basu73@gmail.com", "jlimoeybkwydrepx")
        connection.sendmail(
            from_addr="diya.basu73@gmail.com",
            to_addrs="diya.basu73@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

