#Radhe Radhe
import hashlib
from difflib import SequenceMatcher


def hashfile(file1,file2):
    h1=hashlib.sha1()
    h2=hashlib.sha1()


    with open(file1,"rb") as f1:  #The 'with' statement  makes sure that the file is automatically closed after  the bblock is executed
        chunk=0 #Will store the small parts of the file as wee read it.

        while chunk!=b'':  #b'' => its used o denote an empty byte string.
            chunk=f1.read(1024)  #1024 repfers to bytes i.e , 1kb
           
           #This is generally done to make sure that the  large file is read efficiently without consuming large amount of memory.

            h1.update(chunk)

    with open(file2,"rb") as f2:
        hunk=0

        while hunk!=b'':
            hunk=f2.read(1024)

            h2.update(hunk)


            
