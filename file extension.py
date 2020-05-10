"""
Write a Python program to accept a filename
from the user and print the extension of that.
Sample filename : abc.py Output : py 

@author: dreamy
"""
filename= input("Input filename:")
f_extns=filename.split(".")

print("extension of file is:"+repr(f_extns[-1]))

