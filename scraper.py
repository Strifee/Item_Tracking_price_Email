import requests
from bs4 import BeautifulSoup
import smtplib # module that let you send emails

URL ='https://www.cdiscount.com/telephonie/accessoires-portable-gsm/samsung-galaxy-watch-active-2-40mm-aluminium-gris/f-1442041-samgwatchalu40gr.html#mpos=0|cd' 


headers = {"User-Agent": 'Your use agent'}   # write in google my user agent and copie it in : Your use agent



def price_Track():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')


    title = soup.find('h1',attrs={'itemprop':"name"}).get_text()    # name of the product
    price = soup.find(itemprop="price").get_text()      # price of the priduct
    rounded_price = float(price[0:3])  # 0 -> 3 to get only the first numbers not the dollar signe o

    if(rounded_price < 300):   # the price you want to track 
        sendEmail()
    
    print('PRODUCT: ' + title.strip())
    print('PRICE: ' + price.strip())


     

def sendEmail():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()  #connexion stabiliser 
    s.starttls() #to incript our connexion
    s.ehlo()
    s.login('from@gmail.com','your_passeword')
    subject = 'Price is down !'  #email subject
    body = '''The price of the product you choosed to track is down !   \n\n Link:         
     https://www.cdiscount.com/telephonie/accessoires-portable-gsm/samsung-galaxy-watch-active-2-40mm-aluminium-gris/f-1442041-samgwatchalu40gr.html#mpos=0|cd''' #email body

    msg = f"Subject:{subject}\n\n{body}" # to send the subject + body
    
    s.sendmail('from@gmail.com','To@gmail.com',msg)

    print('EMAIL HAS BEEN SENT SUCCESFULLY !')
    s.quit()

price_Track()