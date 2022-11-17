# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:51:43 2020

@author: chichi
"""
import tkinter as tk
import math
import requests


window = tk.Tk()
window.title('lineNotify')
window.geometry('800x600')
#window.configure(background='white')

def line():
    token="iRdteMVfnkxhkPzUZdh3D2kuzZzjOYUqBeG1cQ-GzDV"
    
    headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
     
    params = {"message": "訊息發送成功!"}
     
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)
    
def IFTTT(title,content,link):
    key="iRdteMVfnkxhkPzUZdh3D2kuzZzjOYUqBeG1cQ-GzDV"    
    url="https://maker.ifttt.com/trigger/line/with/key/"+key+"?value1="+title+"&value2="+content+"&value3="+link
    r = requests.post(url)
    print(r.status_code)

def IFTTT2():
    key="cAYCdvaXFbpzYuwnzmHiEOActive"
    key2="c9665JkAJ_Mf4WEcB_8nmd"
    title=title_entry.get()
    content=content_entry.get("1.0", "end")
    link=link_entry.get()
    url="https://maker.ifttt.com/trigger/line/with/key/"+key2+"?value1="+title+"&value2="+content+"&value3="+link
    r = requests.post(url)
    result_label.configure(text=r.status_code)
    print(r.status_code)


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

calculate_btn = tk.Button(window, text='發送訊息', command=IFTTT2)
calculate_btn.pack()

window.mainloop()
if __name__ == '__main__':
    title="好消息!"
    content="訊息發送成功!"
    link="https://web.cyut.edu.tw/index.php?Lang=zh-tw"
    #IFTTT(title,content,link)
