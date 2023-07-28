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

#creating an email sendeer and reciever
reciever = "my@gmail.com"
sender = "my@gmail.com"
sender_password = "=@123"

#creating functions to send prices
def send_email (sender, reciever, sender_password, text_price):
  #Create a multipart object
  msg = MM()
  msg['Subject'] = "New crypto alert!!!"
  msg['From'] = sender
  msg['To'] = reciever


  #Creating an html for the email
  HTML = """
    <html>
      <body>
        <h1>new crypto alert!</h1>
        <h2>"""+text_price+"""
        </h2>
       </body>
     </html>
     """

  #create html mime text object
  MTObj = MT(HTML, "html")

  #attach the mimetext object
  msg.attach(MTObj)

  #create secure ssl context object
  SSL_context = ssl.create_default_context()

  #create SMTP connection object
  server = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465, context = SSL_context)

  #login to the email
  server.login(sender, sender_password)
  #send the email
  server.sendmail(sender, reciever, msg.as_string())

#create a function to send alert
def send_alert():
  last_price = -1
  #create an infinite loop to send continously
  while True:
    #choose crypto 
    coin = 'bitcoin'
    #get price of cryptocurrency
    price = get_crypto_price(coin)
    #check if it changed
    if price != last_price:
      print(coin.capitalize()+' price: ', price)
      price_text = coin.capitalize()+' is '+price
      send_email (sender, reciever, sender_password, price_text )
      last_price = price #update the price
      time.sleep(3)