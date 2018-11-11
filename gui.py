import tkinter
import tkinter.messagebox
window=tkinter.Tk()
window.geometry('400x300')
window.title('协管员考核管理')
lable=tkinter.Label(window,text='协管员考核管理',font=('微软雅黑',12),width=34,height=2)
lable.pack()
def clickout():
    tkinter.messagebox.showinfo('提示','协管员考核管理')
button1=tkinter.Button(window,text='数据导入',font=('微软雅黑',12),width=15,height=2,command=clickout)
button1.place(x=120,y=60)
tkinter.mainloop()
