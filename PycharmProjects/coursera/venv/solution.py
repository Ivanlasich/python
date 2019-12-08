import sys


class FileReader:
 def __init__(self, name):
     self.name = name
 def read(self):
     try:
        f = open(self.name, 'r+')
        return f.read()
     except IOError:
         return ''




a = FileReader(r'C:\Users\lasic\PycharmProjects\hello\ex.txt')
print(a.read())