import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os

win1 = tk.Tk()  # 常见窗口对象
win1.title('批量命名文件工具')  # 添加窗体名称
win1.geometry('370x280')  # 设置窗体大小

folder_path=""
name=""
num=""

def msgboxCallBack():
    messagebox.showinfo("窗体名","执行完毕")


def getString():
    global folder_path,name,num
    folder_path= te.get()
    name=te1.get()
    num=te2.get()
    n=name1()
    if n==1:
        msgboxCallBack()

def name1():
    count = 1
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # 获取文件扩展名
            file_extension = os.path.splitext(filename)[1]
            # 构建新文件名，序号部分使用格式化保证序号位数统一（比如001这种格式）
            uu = "{:0" + num + "d}{}"
            new_filename = name + uu.format(count, file_extension)
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            count += 1
    return 1

frameroot=Frame(win1)
frameroot.pack(pady=40)

frame=Frame(frameroot)
frame.pack()


lab = Label(frame, text="请输入要重命名的文件夹路径:")
lab.pack(side=LEFT,pady=5)

te = tk.Entry(frame)
te.pack(side=LEFT,pady=5)

frame1=Frame(frameroot)
frame1.pack()

lab1 = Label(frame1, text="请输入要修改后的前缀:")
lab1.pack(side=LEFT,pady=5)

te1 = tk.Entry(frame1)
te1.pack(side=LEFT,pady=5)

frame2=Frame(frameroot)
frame2.pack()

lab1 = Label(frame2, text="请输入要生成的编号为几位数:")
lab1.pack(side=LEFT,pady=5)

te2 = tk.Entry(frame2)
te2.pack(side=LEFT,pady=5)



frame3=Frame(frameroot)
frame3.pack()



Button(frame3, text="运行", command=getString,width=10).pack(pady=5)  # 添加第一个按钮






win1.mainloop()  # 执行窗体
