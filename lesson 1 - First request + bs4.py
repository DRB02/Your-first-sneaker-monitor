#Here we import python modules. Python modules help to make the coding process faster and easier.
import requests
from bs4 import BeautifulSoup
import time

#Here we make a variable for the site URL we going to use
url = 'https://eflash.doverstreetmarket.com/'

#Here we set a variable OUTSIDE the loop. If we would put it inside the loop it would reset the value every time the loop ran. 
last_status = ''
#Start of a while loop https://www.w3schools.com/python/python_while_loops.asp
while True:
    #We added this now so later on we can debug the code easier. https://www.w3schools.com/python/python_try_except.asp
    try:
        #We use the request module in python to get the source of the link in "url".
        page_source = requests.get(url)
        #Here we use BeautifulSoup to convert the page_source to readable text for BeautifulSoup
        page_text = BeautifulSoup(page_source.text,"lxml")
        #We start an if-else statement to check if the page title we got through BeatifulSoup contains "OpeningSoon". 
        #This is very important please read into this. https://www.w3schools.com/python/python_conditions.asp
        if 'Opening Soon' in page_text.title.text:
            #Sets variable pw_status
            pw_status = "Password Page Up"
            #If pw_status is not the same as the variable we set outside of the loop. Run the following:
            if pw_status != last_status:
                #Prints the pw_status and url in console.
                print(pw_status,url)
                #Sets the variable outside of the loop to the current status
                last_status = pw_status

        else:

            pw_status = "Password Page Down"

            if pw_status != last_status:

                print(pw_status,url)

                last_status = pw_status
        #Using the time module to wait 10 seconds for trying again
        time.sleep(10)
    #If the code runs into an error. It runs the following:
    except:
        print('Error requesting to site')
        time.sleep(5)


#simplefied version of https://github.com/TUXCMD/Shopify-PW-Monitor