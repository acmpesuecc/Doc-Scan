import hashlib

file1 = open('file1.avi', 'r').read()
file2 = open('file2.avi', 'r').read()

if hashlib.sha512(file1).hexdigest() == hashlib.sha512(file2).hexdigest():
  print('They are the same')
else:
  print('They are different')

