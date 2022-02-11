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

os.system("figlet -SMS GONDERME ARACI-")

banner = """
         	       ->> Coder By Canpolatgkky <<-


|> İstediginiz Telefon Adresine Hergun 1 Defa Mesaj Atma Hakkınız Vardır !

|> Mesajınızdaki Karakter Sayısı Sınırlıdır.

|> Telefon Adresinizi Doğru Giremesseniz Hata Vericektir.

|> Çalıştığını Kendinizde Deneyebilirsiniz.



|> Telegram = androedit
|> İnstagram = canpolatgkky
"""

print(banner)

sor = input("Telefon Adresi Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız Tekrar Deneyiniz..")
