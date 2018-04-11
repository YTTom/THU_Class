# -*- coding: utf-8 -*-
import urllib3
import os,time,requests,sys,datetime
from bs4 import *

url_A='https://api.thingspeak.com/channels/241665/feeds/last.xml?timezone=Asia/Taipei'

html=requests.get(url_A)
html.encoding='utf-8'
sp=BeautifulSoup(html.text,'html.parser')

tab_66=sp.find("feed")
time=tab_66.find("created-at").string

date=time.replace("-","/")
nid=tab_66.find("entry-id").string
hum=tab_66.find("field1").string
temp=tab_66.find("field2").string
PM25=tab_66.find("field3").string
PM10=tab_66.find("field4").string

print SiteName,AQI,Pollutant,Status,SO2,CO,O3,PM10,PM25,NO2

