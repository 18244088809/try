from tkinter import *
from tkinter import messagebox
import requests
import re

def sign():
    #获取用户输入的姓名
    name = entry.get()
    #去空格
    name = name.strip()
    if name == '':
        messagebox.showinfo('提示',message='请输入姓名!')
    else:
        #获取图片
        data = {
            'word':name,
            'sizes':'60',
            'fonts':'ifcs.ttr',
            'fontcolor':'#000000'
        }

        url = 'http://www.uuu.com/'

        result = requests.post(url,data)
        #设置编码
        result.encoding = 'utf-8'
        #获取页面源代码
        html = result.text
        #<Response [200]>   状态码 请求成功
        print(html)
        #正则表达式                          .*? 匹配所有
        reg = r'<div class="tu">﻿<img src="(.*?)"/></div>'
        imgpath = re.findall(reg,html)
        print(f"{imgpath}")
#创建窗口 root=窗口的对象
root = Tk()
#窗口大小
root.geometry('550x300+200+200')
#窗口的标题
root.title('四则运算')
#标签控件
lable = Label(root,text=":",font=('华文行楷',20),fg='pink')
lable.grid()#定位
#输入框
entry = Entry(root,font=('微软雅黑',20))
entry.grid(row = 0,column = 1)
#点击按钮
button = Button(root,text='设计签名',command=sign)
button.grid(row = 1,column = 1)
#显示窗口
root.mainloop()
