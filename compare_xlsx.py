import pandas as pd
  
sheet1 = pd.read_excel(r'Book1.xlsx')
sheet2 = pd.read_excel(r'Book2.xlsx')

for i,j in zip(sheet1,sheet2):
    
    a,b =[],[]
  
    for m, n in zip(sheet1[i],sheet2[j]):
  
        a.append(m)
        b.append(n)
  
    a.sort()
    b.sort()
  
    for m, n in zip(range(len(a)), range(len(b))):
        if a[m] != b[n]:
            print('Column name : \'{}\' and Row Number : {}'.format(i,m))