from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

i=1
f = open("C_data.csv","w",newline='\n')
write_obj = csv.writer(f)



while i <= 9:
    url = "https://coinmarketcap.com/" + "?page=" + str(i)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    crypto_v = soup.find_all("span",class_="ggzdxp-1 ftvydZ")
    crypto_n = soup.find_all("p",class_="sc-1eb5slv-0 iJjGCS")
    crypto_name = [item.text for item in crypto_n]
    crypto_value = [item.text for item in crypto_v]
    for coins in crypto_n,crypto_v:

       crypto_name = [item.text for item in crypto_n]
       crypto_value = [item.text for item in crypto_v]
    write_obj.writerow([crypto_name,":",crypto_value])
    i += 1
    sleep(5)






