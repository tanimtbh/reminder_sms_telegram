from twilio.rest import Client 
from datetime import date
import requests

team = {  "Juman": {'number': '+46761527686', 'teleid': '1070237010', 'date': [1,2,3,4,5]},
          "Sobur": {'number': '+46738752094', 'teleid': '1036242036', 'date': [6,7,8,9,10]},
          "Rasel": {'number': '++46738752087', 'teleid': '1647390491', 'date': [11,12,13,14,15]},
          "Ferdaws": {'number': '+46727771816', 'teleid': '1476835755', 'date':[16,17,18,19,20]},
          "Zillu": {'number': '+46769382822', 'teleid': '1542478427','date':[21,22,23,24,25]},
          "Tanim": {'number': '+46734838088', 'teleid': '1455603038','date': [26,27,28,29,30]}
       }


 
def send_sms(to, messeage):
    account_sid = 'twilio_sid 487eaeaa4f3d04b3d8192d45' 
    auth_token = 'twilio_auth_token_68269d0c974f869377a' 
    client = Client(account_sid, auth_token)
 
    message = client.messages.create(  
                              messaging_service_sid='MG1d1b8ea59257da55f94d17c8c53fa34e', 
                              body="❤️"+messeage.upper() +"! its A Cleaning Reminder. Today is "+str(date.today())+", Thank you for your cooporation 🙏 ☆☆☆",      
                              to=to 
                          ) 
 
    
    
def send_telegram(message, to):
    uri="https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={}&text={}".format(to, message)
    
    try:
        r = requests.get(
            url=uri,
            headers = {
                "Content-Type":"application/json",
                "Accept":"application/json",
            },
        )
        
        return r.content
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')

def task():
    tday = date.today()
    mydate=str(tday).split("-")
    mydate=int(mydate[2])

    for name, data in team.items():
        print(name)
        if mydate in team[name]['date']:
            print("@@@You Have to clean")
            to=team[name]['teleid']
            send_sms(str(team[name]['number']),name)
            pmessage="❤️"+name.upper() +"! its A Cleaning Reminder. Today is "+str(date.today())+", Thank you for your cooporation 🙏 ☆☆☆"
            send_telegram(pmessage,to)
            gmessage="its time for "+name.upper() +"! A Cleaning Reminder. Today is "+str(date.today())+", Thank you for your cooporation and helping others 🙏 ☆☆☆"
            send_telegram(gmessage,"-467497612")
        print("------------------")