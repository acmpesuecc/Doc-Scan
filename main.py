from pdf2text import pdf2text
from comparetext import comparetext

choice = input("Enter the choice : ")
if(choice == "pdf"):
    c = input("Enter the first pdf file : ")
    d = input("Enter the second pdf file : ")
    pdf2text(c, d)
elif(choice == "text"):
    a = input("Enter first file name : ")
    b = input("Enter second file name : ")
    comparetext(a, b)
