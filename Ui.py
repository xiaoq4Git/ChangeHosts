#-*- coding=utf-8 -*-
from Tkinter import *


def replace(host):
    i = 0
    f = open('C:\Windows\System32\drivers\etc\hosts', 'r+')
    flist = f.readlines()
    for line in flist:
        if "codoon" in line:
            if len(host) > 0:
                if line.startswith("#"):
                    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
                    for ip in reip.findall(line[1:]):
                        line_n = line[1:].replace(ip, host)
                        flist[i] = line_n
                        print(line_n)
                        # return line_n
                else:
                    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
                    for ip in reip.findall(line):
                        line_n = line.replace(ip, host)
                        flist[i] = line_n
                        print(line_n)
                        # return line_n
            else:
                if line.startswith("#"):
                    pass
                    print(line)
                    # return line
                else:
                    line_n = "#" + line
                    flist[i] = line_n
                    print(line_n)
                    # return line_n
        i += 1
    f.close()
    f = open('C:\Windows\System32\drivers\etc\hosts', 'w+')
    f.writelines(flist)
    f.close()

def sel():
    if var.get()==1:
        context = "120.26.17.34 (Testall 环境)"
        selection = "It has changed " + context
        replace('120.26.17.34')
    elif var.get()==2:
        context = "120.26.17.29 (Online 环境)"
        selection = "It has changed " + context
        replace('120.26.17.29')
    else:
        selection = "It has changed 正式环境"
        replace('')
    label.config(text = selection)

root = Tk("test")
root.geometry('400x150')
root.title(u'一键切换测试环境 --V1.0  By 咕咚')
root.iconbitmap('codoon.ico')

var = IntVar()
R1 = Radiobutton(root, text="Testall 环境", variable=var, value="1",command=sel)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Online 环境", variable=var, value=2,command=sel)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="正式环境", variable=var, value=3,command=sel)
R3.pack(anchor=W)

label = Label(root)
label.pack()
root.mainloop()