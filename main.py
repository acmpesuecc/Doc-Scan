from pdf2text import pdf2text
# from comparetext import comparetext
from tkinter import *

root = Tk()
root.geometry("800x800")

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

    # print("Common Lines in Both Files")
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



myLabel = Label(root,text="Enter the choice :")
myLabel.pack()


choice_entry= Entry(root, width= 40)
choice_entry.pack()



button = Button(root,text = "Enter", command= get_data).pack()




root.mainloop()