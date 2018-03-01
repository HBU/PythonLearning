import tkinter as tk
import pymssql
print ("start:")
conn = pymssql.connect(host='.',user='sa',password='sql',database='Test', charset="GBK")
# conn = pymssql.connect('127.0.0.1','sa','sql','Test')
print ("connected!")

cur=conn.cursor()
cur.execute('select top 5 * from [dbo].[S]')
#如果update/delete/insert记得要conn.commit()#否则数据库事务无法提交

list = cur.fetchall()
print (list)
cur.close()
conn.close()

window = tk.Tk()
window.title('my window')
window.geometry('800x400')

var = tk.StringVar() #设置var为tk中的StringVar变量
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=500,height=2) #设置标签文字为var，注意要把text改为textvariable
l.pack()

on_hit = False #设置变量on_hit用来表示标签文字状态，False表示空，True表示非空
def hit():
    global on_hit
    if on_hit == False: #如果标签文字为空
        var.set(list[0]+list[1]+list[2]) #将其设为'my label'
        on_hit = True #更新标签文字状态
    else: #否则
        var.set('') #将其设为空
        on_hit = False #更新标签文字状态

b = tk.Button(window,text='my button',width=15,height=15,command=hit) #点击时执行hit函数
b.pack()

window.mainloop()