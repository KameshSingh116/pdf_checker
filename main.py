#Radhe Radhe
import hashlib
from difflib import SequenceMatcher


def hashfile(file1, file2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(file1, "rb") as f1:  # The 'with' statement makes sure that the file is automatically closed after the block is executed
        chunk = 0  # Will store the small parts of the file as we read it.

        while chunk != b'':  # b'' => it's used to denote an empty byte string.
            chunk = f1.read(1024)  # 1024 refers to bytes i.e., 1kb
           
           # This is generally done to make sure that the large file is read efficiently without consuming large amounts of memory.

            h1.update(chunk)

    with open(file2, "rb") as f2:
        hunk = 0  # Fixed variable name from 'hunk' to 'chunk' to maintain consistency.

        while hunk != b'':
            hunk = f2.read(1024)

            h2.update(hunk)

        return h1.hexdigest(), h2.hexdigest()  # hexdigest() converts the hash values of the files into a sequence of hexadecimal codes/symbols.


message1, message2 = hashfile("C:/Users/lenovo/Desktop/pdf1.pdf", "C:/Users/lenovo/Desktop/pdf3.pdf")

if message1 != message2:
    print("The files are not identical!!!!")

else:
    print("The files are identical!!!!")
