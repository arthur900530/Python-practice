from tkinter import *
from pytube import YouTube

def load():
    vlink = 'https://www.youtube.com/watch?v='
    vlink = vlink + links.get()
    f = folder.get()
    yt = YouTube(vlink)
    x.set('開始下載...')
    yt.streams.filter(progressive=True, res='720p').last().download(f)
    x.set('下載完成')


window = Tk()
window.title('Youtube Downloader')
window.geometry('400x250')

x = StringVar()
x.set('請輸入檔案序列碼')
links = StringVar()
folder = StringVar()

l1 = Label(window, text='輸入檔案序列碼: ').grid(row=0)
l2 = Label(window, text='輸入目標資料夾: ').grid(row=1)
l3 = Label(window,textvariable=x, height=3).grid(row=2, column=0, columnspan=2)

e1 = Entry(window, textvariable=links)
e2 = Entry(window, textvariable=folder)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = Button(window, text='下載', command=load)
btn1.grid(row=3,column=0)
btn2 = Button(window, text='結束', command=window.destroy)
btn2.grid(row=3,column=1)

window.mainloop()