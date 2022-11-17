# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:51:43 2020

@author: chichi
"""
from asyncio import events
import tkinter as tk
import math
import requests


window = tk.Tk()
window.title('lineNotify')
window.geometry('650x300')
#window.configure(background='white')
header_label = tk.Label(window, text='line通知')
header_label.pack()

title_frame = tk.Frame(window)
title_frame.pack(side=tk.TOP)
title_label = tk.Label(title_frame, text='主題')
title_label.pack(side=tk.LEFT)
title_entry = tk.Entry(title_frame,width=100)
title_entry.pack(side=tk.LEFT)

content_frame = tk.Frame(window)
content_frame.pack(side=tk.TOP)
content_label = tk.Label(content_frame, text='內容')
content_label.pack(side=tk.LEFT)
content_entry = tk.Text(content_frame,width=100,height=10)
content_entry.pack(side=tk.LEFT)

link_frame = tk.Frame(window)
link_frame.pack(side=tk.TOP)
link_label = tk.Label(link_frame, text='連結')
link_label.pack(side=tk.LEFT)
link_entry = tk.Entry(link_frame,width=100)
link_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

def line_notify():
    token = "輸入你的token"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
        }    
    params = {"message": "訊息發送成功!"}
    
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
    print(r.status_code)
    return r.status_code
    
def IFTTT_line_notify(event, title, content, link):  
    """
    IFTTT
    If WebHook receive a web request
    Then Line send message
    """
    key = "輸入你的key"  
    url = f"https://maker.ifttt.com/trigger/{event}/with/key/{key}?value1={title}&value2={content}&value3={link}"
    r = requests.post(url)
    print(r.status_code)
    return r.status_code

def send_message():
    title=title_entry.get()
    content=content_entry.get("1.0", "end")
    link=link_entry.get()
    event = 'line_notify'
    IFTTT_line_notify(event, title, content, link)

calculate_btn = tk.Button(window, text='發送訊息', command=send_message)
calculate_btn.pack()   

window.mainloop()
