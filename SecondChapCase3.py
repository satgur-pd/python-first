'''
Case Study – 3
Domain –Telecom
focus – Optimization

Key issues
Build a system where when a user enters Reference ID it is encrypted so that hackers 
cannot view the mapping of Reference ID and fingerprint

Approach to Solve
You must use the fundamentals of Python taught in module 1
1. Read the input from the command line - Reference ID
2. Check for validity - it should be 12 digits and allows for number and alphabet
3. Encrypt the Reference ID and print it for reference

Enhancements for code
You can try these enhancements in code
1. Allow some special characters in ReferenceID
2. Give the option for decryption to the user

'''

from cryptography.fernet import Fernet
import re

def checkValidId(refId):
    matcher = bool(re.match('[a-zA-Z0-9$#@*_%]{12}',refId) and (len(refId)==12) )
    return matcher 

_usrid_input = input("Enter Reference Id for your SIM -> ")

if (checkValidId(_usrid_inp)==True):
    key = Fernet.generate_key()
    f_obj = Fernet(key)

    encrypted_msg = f_obj.encrypt(_usrid_input)
    print(f"Encrypted reference id is --> {encrypted_msg}")

    _q2 = input("Do you want get decrypted id back (y/n)?")

    if (_q2=="Y" or 'y'):
        decrypted_msg = f_obj.decrypt(encrypted_msg)
        print(f"Your reference id is ==> {decrypted_msg}")

