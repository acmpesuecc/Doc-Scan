import PyPDF2


def pdf2text(c, d):
    pdfFileObj1 = open(c, 'rb')
    pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
    for i in range(pdfReader1.numPages):
        pageObj1 = pdfReader1.getPage(i)

    pdfFileObj2 = open(d, 'rb')
    pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)
    for i in range(pdfReader2.numPages):
        pageObj2 = pdfReader2.getPage(i)

    count = 0
    l = len((pageObj1.extractText()).split())
    for i in range(l):
        if (((pageObj1.extractText()).split())[i] == (
                (pageObj2.extractText()).split())[i]):
            count = count+1
        elif (((pageObj1.extractText()).split())[i] != (
                (pageObj2.extractText()).split())[i]):
            print(((pageObj1.extractText()).split())[
                  i], ((pageObj2.extractText()).split())[i], "There is a mistake at", i, "word")
    rem = l-count
    print("The number of mistakes are : ", rem)
    pdfFileObj1.close()
    pdfFileObj2.close()
