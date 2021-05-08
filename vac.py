#Chwechy ki vaccine dedo bhaiya

import requests

import json
import datetime
from datetime import date
import time
import sched

import tkinter
from tkinter import messagebox


def alerter (i,j,ismsg,num):
    msg= (str(j["available_capacity"]) + " slot(s) available for " +j["vaccine"]+ " on "+j["date"] +  " at "+i["name"]+" Addr- "+i["address"] + " for ages "+str(j["min_age_limit"]) +" and above")
    titl=j["vaccine"]+ " slot  available " 
    print(msg)
    if ismsg=="1":
        root = tkinter.Tk() 
        root.withdraw()
        messagebox.showinfo(titl, msg)
    if num!="-1":
        url = "https://rest-api.d7networks.com/secure/send"
        payload = "{\n\t\"to\":\"91"+str(num)+"\",\n\t\"content\":\""+msg+"\",\n\t\"from\":\"VACINFO\",\n\t\"dlr\":\"yes\",\n\t\"dlr-method\":\"GET\", \n\t\"dlr-level\":\"2\", \n\t\"dlr-url\":\"http://yourcustompostbackurl.com\"\n}"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic aWt2cDk3NjU6REtVNlUyQ3M='
            }

    response = requests.request("POST", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    try:
        import winsound
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    except:
        print('\a')
    
        
    
pin=input("Enter your pincode ")
ismsg=input ("Do you want message box updates ? (1 for yes, 0 for no) ")
num=input ("Do you want SMS updates? (type -1 for no, your mobile number for yes) ")
loop=input ("Do you want continous looping ? (1 for yes, 0 for no) ")

for x in range(0,21,7):    
    today= date.today()+ datetime.timedelta(days=x)
    parameters ={
        "pincode":pin ,
        "date": today.strftime("%d-%m-%Y") }
    resp=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin",params=parameters)
    if resp.status_code==200 and len(resp.json()["centers"])>0:
        data=resp.json()
        for i in data["centers"]:
            for j in i["sessions"]:
                if (j['available_capacity']>0):
                    alerter(i,j,ismsg,num)
                    
while loop=="1" :
         for x in range(0,21,7):    
             today= date.today()+ datetime.timedelta(days=x)
             parameters ={
                 "pincode":pin ,
                 "date": today.strftime("%d-%m-%Y") }
         resp=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin",params=parameters)
         if resp.status_code==200 and len(resp.json()["centers"])>0:
             data=resp.json()
             for i in data["centers"]:
                 for j in i["sessions"]:
                     if (j['available_capacity']>0):
                         alerter(i,j,ismsg,num)
         time.sleep(5)
    