#Description: This program sends crypto currency price alerts
#Import the libraries
from bs4 import BeautifulSoup
import requests
import time 
import smtplib
import ssl
from email.mime.text import MIMEText as MT 
from email.mime.multipart import MIMEMultipart as MM

#Create a function to get the price of a cryptocurrency
def get_crypto_price (coin):
    #Get the URL
    url = "https://www.google.com/search?q="+coin+"+price"

    #Make a request to the website
    HTML = requests.get (url)

    #Parse the HTML
    soup = BeautifulSoup (HTML. text, 'html.parser')

    #Find the current price
    text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    #Return the text return text
    return text

