# -*- coding: utf-8 -*-
import urllib3
import os,time,requests,sys,datetime
reload(sys)#重要編碼
from threading import Timer
from datetime import date
from bs4 import *

sys.setdefaultencoding('utf8')

url='http://taqm.epb.taichung.gov.tw/aqi/aqiNEW.ASPX?name=6'

html=requests.get(url)
html.encoding='utf-8'
sp=BeautifulSoup(html.text,'html.parser')

print sp


SiteName=sp.find_all('td')[3].string[0:2]
AQI=sp.find_all('td')[5].string
Pollutant=sp.find_all('td')[6].string
Status=sp.find_all('td')[4].string
SO2=sp.find_all('td')[8].string
CO=sp.find_all('td')[10].string
O3=sp.find_all('td')[12].string
PM10=sp.find_all('td')[14].string
PM25=sp.find_all('td')[18].string
NO2=sp.find_all('td')[16].string

print SiteName,AQI,Pollutant,Status,SO2,CO,O3,PM10,PM25,NO2