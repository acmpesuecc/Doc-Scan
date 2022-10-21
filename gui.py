import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
def file1():
    my_w = tk.Tk()
    my_w.geometry("400x300")  # Size of the window 
    my_w.title('Doc-Scan')
    my_font1=('times', 18, 'bold')
    l1 = tk.Label(my_w,text='upload file 1',width=30,font=my_font1)  
    l1.grid(row=1,column=1)
    b1 = tk.Button(my_w, text='Upload File', 
    width=20,command = lambda:upload_file())
    b1.grid(row=2,column=1)
def file2():
    my_w = tk.Tk()
    my_w.geometry("400x300")  # Size of the window 
    my_w.title('Doc-Scan')
    my_font1=('times', 18, 'bold')
    l1 = tk.Label(my_w,text='upload file 2',width=30,font=my_font1)  
    l1.grid(row=1,column=1)
    b1 = tk.Button(my_w, text='Upload File', 
    width=20,command = lambda:upload_file())
    b1.grid(row=2,column=1)
 




