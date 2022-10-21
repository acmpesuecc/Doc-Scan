
from pdf2text import pdf2text
import cv2
import numpy as np
from comparejpg import compare_images
from tkinter import *

root = Tk()
root.geometry("800x800")

import collections 
import collections.abc
from pptx import Presentation


def compare_images(img1, img2):
    a = cv2.imread(img1)
    b = cv2.imread(img2)
    difference = cv2.subtract(a, b)    
    result = not np.any(difference)
    if result is True:
        print("Pictures are the same")
        Label(root,text=f"Pictures are the same").pack()
    else:
        cv2.imwrite("difference.png", difference )
        Label(root,text=f"Pictures are different, the difference is stored as ed.png").pack()
        

def compare_ppt(p1,p2):
    
    ppt1 = Presentation(p1)
    ppt2 = Presentation(p2)

    text_runs1 = []
    text_runs2 = []

    for slide in ppt1.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs1.append(run.text)
    for slide in ppt2.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs2.append(run.text)
    if collections.Counter(text_runs1) == collections.Counter(text_runs2):
        Label(root,text=f"The presentations are same").pack()
        
    else:
        Label(root,text=f"The presentations are different").pack()
        Label(root,text=f"The differences are : ").pack()
        Label(root,text=collections.Counter(text_runs1) - collections.Counter(text_runs2)).pack()
       




def comparetext(a, b):
    file_1 = open(a, 'r')
    file_2 = open(b, 'r')

    file_1_line = file_1.readline()
    file_2_line = file_2.readline()

    line_no = 1

    print()

    with open('text1.txt') as file1:
        with open('text2.txt') as file2:
            same = set(file1).intersection(file2)

    #print("Common Lines in Both Files")
    Label(root,text=f"Common Lines in Both Files").pack()

    for line in same:
        # print(line, end='')
        Label(root,text=f"{line} ").pack()

    print('\n')
    Label(root,text=f"Difference Lines in Both Files").pack()
    # print("Difference Lines in Both Files")
    print('\n')
    while file_1_line != '' or file_2_line != '':

        file_1_line = file_1_line.rstrip()
        file_2_line = file_2_line.rstrip()

        if file_1_line != file_2_line:

            if file_1_line == '':
                # print("file1-", "Line-%d" % line_no, file_1_line)
                Label(root,text=f"File1- {line_no} Line- {file_1_line}").pack()
            else:
                # print("file1-", "Line-%d" % line_no, file_1_line)
                Label(root,text=f"File1- {line_no} Line- {file_1_line}").pack()

            if file_2_line == '':
                # print("file2-", "Line-%d" % line_no, file_2_line)
                Label(root,text=f"File2- {line_no} Line- {file_2_line}").pack()
            else:
                # print("file2-", "Line-%d" % line_no, file_2_line)
                Label(root,text=f"File2- {line_no} Line- {file_2_line}").pack()

            print()

        file_1_line = file_1.readline()
        file_2_line = file_2.readline()

        line_no += 1

    file_1.close()
    file_2.close()



def get_data():
    choice = choice_entry.get()
    file1_entry = Label(root,text="Enter File 1 Name :")
    file1_entry.pack()
    file1_entry = Entry(root, width= 40)
    file1_entry.pack()

    file2_entry = Label(root,text="Enter File 2 Name :")
    file2_entry.pack()
    file2_entry = Entry(root, width= 40)
    file2_entry.pack()
    if(choice == "pdf"):
        def pdf_check():
            out = pdf2text(file1_entry.get(),file2_entry.get())
            Label(root,text=f"Number of mistakes are : {out}").pack()
        
        Button(root,text = "Enter", command= pdf_check).pack()

    elif(choice == "text"):
        def textcheck():
            comparetext(file1_entry.get(),file2_entry.get())

        Button(root,text = "Enter", command= textcheck).pack()

    elif(choice == "ppt"):
        def pptcheck():
            compare_ppt(file1_entry.get(),file2_entry.get())

        Button(root,text = "Enter", command= pptcheck).pack()
    
    elif(choice == 'image'):
        def imagecheck():
            compare_images(file1_entry.get(),file2_entry.get())
        Button(root,text = "Enter", command= imagecheck).pack()



myLabel = Label(root,text="Enter the choice :")
myLabel.pack()


choice_entry= Entry(root, width= 40)
choice_entry.pack()



button = Button(root,text = "Enter", command= get_data).pack()




root.mainloop()