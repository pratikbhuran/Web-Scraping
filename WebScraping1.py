
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import pandas as pd

my_url= 'https://www.flipkart.com/search?q=mi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off' #link of website to be scraped

client = ureq(my_url)               #giving link to request 
page_html = client.read()           #read the page html
client.close()

page_soup = soup(page_html, "html.parser")  #parsing the html of page

containers = page_soup.findAll("div", {"class" :"_3O0U0u"})     #HTML tag that contain the needed information
print("The number of components is ")
print (len(containers))                #no. of components in the tag 
#print(soup.prettify(containers[0]))    #prettify the html and print the specified component

n = int(input("what is the range"))
for i in range(n):
    container = containers[i]
    print(container.div.img["alt"])      #print the attribute needed(name) of the component

    price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})  #tag and class containing price
    print(price[0].text)
#file= "getdata.csv"
#f=open(file, "w")

#headers="Product_name,Pricing \n"
#f.write(headers)



