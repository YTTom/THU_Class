# -*- coding: utf-8 -*-
import urllib3
import os,time,requests,sys,datetime
from bs4 import *

url = "http://taqm.epb.taichung.gov.tw/TQAMNEWAQITABLE.ASPX"
html=requests.get(url)
sp=BeautifulSoup(html.text,'html.parser')

SiteName=sp.find_all('td')[3].string
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
