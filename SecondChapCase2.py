'''1. What is the output of the following code?
nums = set([1,1,2,3,3,3,4,4])
print(len(nums))'''

#Answer is 4 which shows site of SET. 
#Since SET contains only unique items, it will have (1,2,3,4)

#--------------------------------------------------------------------------------

'''2. What will be the output?
d = {"john":40, "peter":45}
print(list(d.keys()))
Hint: d.keys() is the function that will show keys.'''

#Answer is ['john','peter']

#--------------------------------------------------------------------------------

'''3. A website requires a user to input a username and password to register. Write a 
program to check the validity of the password given by the user. Following are the 
criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Hint: In the case of input data being supplied to the question, it should be assumed to 
be a console input.'''

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

    error_msg = 'Password guideline(s) not followed : '

    if (num_Check==False):
        #print("Password should contain DIGITS 0-9...")
        error_msg+="\n\tPassword should contain DIGITS 0-9..."
    if(small_Letter_Check==False):
        #print("Password should contain small case [a-z] letters..")
        error_msg+="\n\tPassword should contain small case [a-z] letters.."
    if(caps_Num_Check==False):    
        #print("Password should contain Capital [A-Z] letters..")
        error_msg+="\n\tPassword should contain Capital [A-Z] letters.."
    if(special_Char_Check==False):
        #print("Password should contain Special Characters[#$@]...")
        error_msg+="\n\tPassword should contain Special Characters[#$@]..."
    if (num_Check==True & small_Letter_Check==True & caps_Num_Check==True & special_Char_Check==True):
        print("Congratulations!! Your password {} has been successfully set.".format(__usrPassword))   
    else:
        print(error_msg)

#--------------------------------------------------------------------------------

'''4. Write a for loop that prints all elements of a list and their position in the list.
 a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements.'''

usr_inp=input('Enter a set of values separated by space -> ')
lst_inp_items = usr_inp.split()
j=0
for i in lst_inp_items:
    print(j,i)
    j+=1

#--------------------------------------------------------------------------------

'''5. Please write a program that accepts a string from the console and print the 
characters that have even indexes.
 Example: If the following string is given as input to the program:
 H1e2l3l4o5w6o7r8l9d
 Then, the output of the program should be:
 Helloworld'''

usr_inp = input("Enter a sentence --> ")
j=0
out_str = ""

for c in usr_inp:
    if (j%2 == 0):
        out_str += c
    j+=1
print(out_str)

#--------------------------------------------------------------------------------


'''6. Please write a program that accepts a string from the console and print it in reverse 
order.
 Example: If the following string is given as input to the program: 
 rise to vote sir
 Then, the output of the program should be:
 ris etov ot esir'''

usr_inp = input("Enter a sentence --> ")
j=0
k=len(usr_inp)
out_str =""

for i in range(0,k):
    out_str+=usr_inp[(-1-i)]

print(out_str)

#--------------------------------------------------------------------------------

'''
7. Please write a program that counts and prints the numbers of each character in a 
string input by the console.
 Example: If the following string is given as input to the program:
 abcdefgabc
 Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1 '''

usr_inp = input("Enter some text here --> ")
_val_set = set(usr_inp)

out_str=''

for c in _val_set:
    _count = usr_inp.count(c)
    out_str+="\n"+c+","+str(_count)    

print(out_str)

#--------------------------------------------------------------------------------


'''
8. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a 
program to make a list whose elements are intersection of the above given lists.
'''

listA = [1,3,6,78,35,55]
listB = [12,24,35,24,88,120,155]

setA = set(listA)
setB = set(listB)

setC = setA.intersection(setB)

listC = list(setC)
print ("intersection of given lists is ==> ", listC)


#--------------------------------------------------------------------------------

'''
9. By using list comprehension, please write a program to print the list after removing 
the value 24 in [12,24,35,24,88,120,155].
'''

listA = [12,24,35,24,88,120,155]
val_remove = 24

listB = [x for x in listA if x!=val_remove]
print(listB)

#--------------------------------------------------------------------------------

'''
10.By using list comprehension, please write a program to print the list after removing 
the 0th,4th, and 5th numbers in [12,24,35,70,88,120,155]
'''

listA = [12,24,35,70,88,120,155]
lst_remove = [12,88,120]

listB = [x for x in listA if x not in lst_remove]
print (listB)

#--------------------------------------------------------------------------------
'''
11.By using list comprehension, please write a program to print the list after removing 
deleted numbers that are divisible by 5 and 7 in [12,24,35,70,88,120,155]
'''
listA = [12,24,35,70,88,120,155]
list_remove = [x for x in listA if (x%5==0 or x%7==0)]
listB = [x for x in listA if x not in list_remove]
print (listB)

#--------------------------------------------------------------------------------
'''
12.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by 
console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
'''

def func_calculateTotal(usr_no):
    _total=0
    tempNo=usr_no
    while tempNo>=1:
        if (tempNo>1):
            _total+=(tempNo/(tempNo+1))
            tempNo -=1
        elif (tempNo==1):
             _total+=(tempNo/(tempNo+1))   
             break
    return _total         


usr_no=input("Enter a number => ")
total_n=0

if int(usr_no) > 0:
    total_n = func_calculateTotal(int(usr_no))
    print(total_n)

#--------------------------------------------------------------------------------
