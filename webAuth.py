'''
3. A website requires a user to input username and password to register. Write a program
to check the validity of password given by user. Following are the criteria for checking
password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
'''
def checkSmallCase(userPWD):
    __small = set(r"""abcdefghijklmnopqrstuvwxyz""")
    for i in userPWD:
        if i in __small:
            return True
    else:
        return False
    
def checkCAPS(userPWD):
    __caps = set(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
    for i in userPWD:
        if i in __caps:
            return True
    else:
        return False

def checkSpecialChar(userPWD): 
    symbols = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")
    for i in userPWD:
        if i in symbols:
            return True
    else:
        return False

def checkNumber(userPWD):
    for i in userPWD:
        if i.isdigit():
            return True
    else:
        return False

__usrPassword = input("Enter passowrd: ")
#print (__usrPassword)

__lengthUsrPWD = len(__usrPassword)
print ("length of password -->", __lengthUsrPWD)

if (__lengthUsrPWD < 6):
    print("Password should be minimum 6 character in length")
elif (__lengthUsrPWD > 12):
    print("Password should be maximum 12 character in length")
else:
    num_Check = checkNumber(__usrPassword)
    small_Letter_Check = checkSmallCase(__usrPassword)
    caps_Num_Check = checkCAPS(__usrPassword)
    special_Char_Check = checkSpecialChar(__usrPassword)

    if (num_Check==False):
        print("Password should contain DIGITS 0-9...")
    elif(small_Letter_Check==False):
        print("Password should contain small case [a-z] letters..")
    elif(caps_Num_Check==False):    
        print("Password should contain Capital [A-Z] letters..")
    elif(special_Char_Check==False):
        print("Password should contain Special Characters[#$@]...")
    else:
        print("Congratulations!! Your password {} has been successfully set.".format(__usrPassword))   

#if (len(__usrPassword))