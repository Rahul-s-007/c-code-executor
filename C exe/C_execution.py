from tkinter import *
from tkinter import filedialog

import os

Tk().withdraw()
filename = filedialog.askopenfilename(initialdir = "C:\\Users\\RAHUL\\Desktop\\C Programs", title = "Select C Program", filetypes = (("c files", "*.c*"), ("all files","*.*")))
# filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files","*.*")))
# C:/Users/RAHUL/Desktop/C Programing/Programs/Hello World/helloworld.c
#print(filename)

l = filename.rfind("/")

dirpath = filename[0:l:1]
#print(dirpath)
flname = filename[l+1:len(filename):1]
#print(flname)
#"""
os.chdir(dirpath)

comd = "gcc -o c_execute {}".format(flname)
#gcc -o c_execute helloWorld.c

os.system(comd)
#gcc -o c_execute helloWorld.c
#"""

os.system("c_execute")

rmpath = dirpath + "/c_execute.exe"
os.remove(rmpath)