import requests
from bs4 import BeautifulSoup
import time
#importing discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed

url = 'https://eflash.doverstreetmarket.com/'
#Here we make a variable for the webhook URL we are going to use.
WebhookUrl = 'INSERT YOUR WEBHOOK HERE'

#message post function
def message_post(pw_status,monitor_store_url):
    #Setting up webhoook link + webhook name
    webhook = DiscordWebhook(url=WebhookUrl, username='Password page')
    #Putting the site url to a string, setting it to title, setting title link to the site and setting the pw status as description.
    embed = DiscordEmbed(title=str(monitor_store_url), description='**'+ pw_status +'**', color=0x00FF00, url=monitor_store_url)
    embed.set_footer(text='https://github.com/DRB02/Your-first-sneaker-monitor')
    embed.set_timestamp()
    #Adding all the embed lines to the webhook.
    webhook.add_embed(embed)
    #Sending the webhook
    webhook.execute()
    #Printing in console when the webhook is successfully sent.
    print('[SUCCESS] --> Successfully sent success webhook!')

last_status = ''
while True:
    try:
        page_source = requests.get(url)
        page_text = BeautifulSoup(page_source.text,"lxml")
        if 'Opening Soon' in page_text.title.text:
            pw_status = ":red_circle: Password Page Up :red_circle:"
            if pw_status != last_status:
                #we start the message post function and send it the info: pw_status and the current url
                message_post(pw_status, url)
                last_status = pw_status

        else:
            pw_status = ":green_circle: Password Page Down :green_circle:"
            if pw_status != last_status:
                message_post(pw_status, url)
                last_status = pw_status
        time.sleep(10)
    except:
        print('Error requesting to site')
        time.sleep(5)


#Look here for more examples of webhook usage: (Run this and check what does what)
#https://github.com/DyBlok/CheatSheets/blob/master/Python/Discord%20webhook.py

#And be sure to check this out if you are interested in more in-depth of this ^
#https://github.com/TUXCMD/Shopify-PW-Monitor
