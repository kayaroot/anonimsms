#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("apt-get update")

os.system("apt-get upgrade")

os.system("apt-get install curl")
           
os.system("apt-get install python")
           
os.system("apt-get install figlet")

os.system("clear")

os.system("figlet KAYA - SMS GONDERME ARACI")

banner = """
         	             >Coder By KAYA
|> İstediginiz telefon numarasına her gun 1 defa mesaj atma hakkınız vardır!
|> Mesajınızdaki karakter sayısı 70'i geçmemelidir.
|> Telefon numarasını doğru girmezseniz hata vericektir.
|> Çalıştığını onaylamak için kendinizde deneyebilirsiniz.
|> Arkadaşlar doğru girdiğiniz halde hata veriyorsa 2. defa tekrar deneyin hata verse bile çalışacaktır.
|> telegram: @hackzafiyetleri
|> instagram: @kaya.root
"""

print(banner)

sor = input("Tel adresi Örn: +905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    import urllib.request
import urllib.parse

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

resp =  sendSMS('apikey', '447123456789',
    'Jims Autos', 'This is your message')
print (resp)

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptın kanka :D")
