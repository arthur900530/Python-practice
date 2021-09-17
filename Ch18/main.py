from tkinter import *

# w = Tk()
# w.geometry('1300x850')
# w.title('Test')
# # w.resizable(0,0)
# l1 = Label(w,text='Hello world',
#            bg='lightyellow',
#            width=10,
#            font='CARTER 30 bold').grid(row=0,column=0)
# l2 = Label(w,text='Hello world',
#            bg='lightgreen',
#            width=10,
#            font='CARTER 30 bold').grid(row=1,column=1)
# l3 = Label(w,text='Hello world',
#            bg='lightblue',
#            width=10,
#            font='CARTER 30 bold',
#            )
# def show():
#     l3['text'] = 'Hi !'
#     l3['bg'] = 'orange'
#     l3['fg'] = 'white'
#
# def yellow():
#     global isYellow
#     if isYellow:
#         w.config(bg='lightblue')
#         isYellow = False
#     else:
#         w.config(bg='yellow')
#         isYellow = True
#
#
# b1 = Button(w,text='Click me',
#             command=show,
#             width='10',
#             font='CARTER 15 bold').place(x=575,y=400)
# b2 = Button(w,text='Exit',
#             command=yellow,
#             width='10',
#             font='CARTER 15 bold').place(x=575,y=480)
# isYellow = False
# e1 = Entry(w)
# e1.insert(2,'KKKKK')
# e1.place(x=550,y=600)
#
# l3.place(x=500,y=300)
#
# w.mainloop()


# w = Tk()
# w.title('Text')
#
# sc = Scrollbar(w)
# text = Text(w, height = 2, width = 30)
# text.insert(END,"我懷念\n一個人的極境旅行")
# str = """2016年12月,我一個人訂了機票和船票,
# 開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
# 在此我登上郵輪開始我的南極之旅"""
# text.insert(END,str)
# sc.pack(side = RIGHT,fill = Y)
# text.pack(side = LEFT,fill = Y)
# sc.config(command = text.yview)
# text.config(yscrollcommand = sc.set)
#
# w.mainloop()

# w = Tk()
# w.title('CB')
# p = PhotoImage(file='color-block.png')
# # Label(w,image=p).pack()
# btn = Button(w, image=p,command=w.destroy)
# btn.pack()
# w.mainloop()
def calculate():  # 執行計算並顯示結果
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))


def show(buttonString):  # 更新顯示區的計算公式
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)


def backspace():  # 刪除前一個字元
    equ.set(str(equ.get()[:-1]))


def clear():  # 清除顯示區,放置0
    equ.set("0")

root = Tk()
root.title('計算器')

equ = StringVar()
equ.set('0')

label = Label(root,width=25,height=2,relief='raised',anchor=SE,textvariable=equ,font='CARTER 20')
label.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

clear = Button(root,text='C',fg='blue',width=5,command=clear,font='CARTER 20')
clear.grid(row=1,column=0)
Button(root,text="DEL",width=5,command=backspace,font='CARTER 20').grid(row=1,column=1)
Button(root,text="%",width=5,command=lambda:show("%"),font='CARTER 20').grid(row=1,column=2)
Button(root,text="/",width=5,command=lambda:show("/"),font='CARTER 20').grid(row=1,column=3)

Button(root,text="7",width=5,command=lambda:show("7"),font='CARTER 20').grid(row=2,column=0)
Button(root,text="8",width=5,command=lambda:show("8"),font='CARTER 20').grid(row=2,column=1)
Button(root,text="9",width=5,command=lambda:show("9"),font='CARTER 20').grid(row=2,column=2)
Button(root,text="*",width=5,command=lambda:show("*"),font='CARTER 20').grid(row=2,column=3)

Button(root,text="4",width=5,command=lambda:show("4"),font='CARTER 20').grid(row=3,column=0)
Button(root,text="5",width=5,command=lambda:show("5"),font='CARTER 20').grid(row=3,column=1)
Button(root,text="6",width=5,command=lambda:show("6"),font='CARTER 20').grid(row=3,column=2)
Button(root,text="-",width=5,command=lambda:show("-"),font='CARTER 20').grid(row=3,column=3)

Button(root,text="1",width=5,command=lambda:show("1"),font='CARTER 20').grid(row=4,column=0)
Button(root,text="2",width=5,command=lambda:show("2"),font='CARTER 20').grid(row=4,column=1)
Button(root,text="3",width=5,command=lambda:show("3"),font='CARTER 20').grid(row=4,column=2)
Button(root,text="+",width=5,command=lambda:show("+"),font='CARTER 20').grid(row=4,column=3)

Button(root,text="0",width=12,
       command=lambda:show("0"),font='CARTER 20').grid(row=5,column=0,columnspan=2)
Button(root,text=".",width=5,
       command=lambda:show("."),font='CARTER 20').grid(row=5,column=2)
Button(root,text="=",width=5,bg ="yellow",
       command=lambda:calculate(),font='CARTER 20').grid(row=5,column=3)

root.mainloop()
