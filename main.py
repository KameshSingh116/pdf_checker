#Radhe Radhe
import hashlib
from difflib import SequenceMatcher


def hashfile(file1,file2):
    h1=hashlib.sha1()
    h2=hashlib.sha1()


    