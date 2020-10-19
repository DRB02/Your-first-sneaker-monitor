#imports of python modules
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
#site the url we will be requesting from. I recommend having a look at the page yourself and see what this script does. 
url = 'http://books.toscrape.com/'

#Setting the webhook URL
#WebhookUrl = ['WEBHOOK1', 'WEBHOOK2']
#use [] to use multiple webhooks
WebhookUrl = 'WEBHOOK URL'

#using headers because a lot of sites require it
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

#message post function for more info see:
# https://github.com/DyBlok/CheatSheets/blob/master/Python/Discord%20webhook.py
def message_post(name, url, PictureLink, price):
    webhook = DiscordWebhook(url=WebhookUrl, username='Books to Scrape')
    embed = DiscordEmbed(title=name, color=0x000000, url=url)
    embed.add_embed_field(name='Price', value=price)
    embed.set_image(url=PictureLink)
    embed.set_footer(text='https://github.com/DRB02/Your-first-sneaker-monitor')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    print('[SUCCESS] --> ' + name)



#requesting the source with python requests and parsing it to lxml for beatifullsoup to use
source = requests.get(url, headers=headers)
soup = BeautifulSoup(source.text,"lxml")
#gets site title
title = soup.title.text
#scrapes all product + info
for Books in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
    name = Books.find('h3').a.get('title')
    href = Books.find('h3').a.get('href')
    #The href is only part of the link here we making it a full link
    url = 'http://books.toscrape.com/'+href
    picture = Books.find('img').get('src')
    PictureLink = 'http://books.toscrape.com/'+picture
    #An other way to do it. Searching on attributes
    price = Books.find(attrs={'class':'price_color'}).text.strip('Â')
    #While scraping the prices load with having a 'Â' in front of it. We used .strip() to remove that specif character
    #You can also leave the strip function empty and it will remove all the spaces from the text.

    #sending the webhook
    message_post(name, url, PictureLink, price)
    #delay to avoid ratelimit
    time.sleep(0.5)

