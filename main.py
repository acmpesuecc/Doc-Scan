from pdf2text import pdf2text
from comparetext import comparetext
from tkinter import *



def get_data():
    choice = choice_entry.get()
    if(choice == "pdf"):
        file1_entry = Label(root,text="Enter File 1 Name :")
        file1_entry.pack()
        file1_entry = Entry(root, width= 40)
        file1_entry.pack()

        file2_entry = Label(root,text="Enter File 2 Name :")
        file2_entry.pack()
        file2_entry = Entry(root, width= 40)
        file2_entry.pack()

        def pdf_check():
            out = pdf2text(file1_entry.get(),file2_entry.get())
            Label(root,text=f"Number of mistakes are : {out}").pack()
        
        Button(root,text = "Enter", command= pdf_check).pack()

        
    elif(choice == "text"):
        a = input("Enter first file name : ")
        b = input("Enter second file name : ")
        comparetext(a, b)



root = Tk()

root.geometry("500x500")

myLabel = Label(root,text="Enter the choice :")
myLabel.pack()


choice_entry= Entry(root, width= 40)
choice_entry.pack()



button = Button(root,text = "Enter", command= get_data).pack()




root.mainloop()