#this is assignment for first chapter from Python Curriculum

#------------------------------------------------------------------------------------
#case study 1
""" Write a program which will find factors of given number and find whether the
factor is even or odd. """

def findfactors(_no_int):
    #inside findfactors method
    factors = []
    count = 1

    while count <= _no_int:   
        #print("count = ", count)
        if _no_int%count == 0:
            factors.append(count)
            count+=1        
            #print("factors = ", factors)    
        else:  
            count+=1     
            continue    

    return factors

while (True):
    _user_no = int(input("Enter a whole number : "))

    if (_user_no==1):
        print("Thanks for playing with me !!")
        break
    else:
        print("you entered - ", _user_no)
    
    _lst_factors = findfactors(_user_no)

    for _factor in _lst_factors:
        if _factor%2 == 0:
            print("Factor " + str(_factor) + " is an EVEN number")
        else: 
            print("Factor " + str(_factor) + " is an ODD number")

#--------------------------------------------------------------------------------------

""" case study 2. Write a code which accepts a sequence of words as input and prints the words in a
sequence after sorting them alphabetically.  

""" 
x=1
while (x==1):
    words = input("Enter sequence of words : ")
    lst_words = words.split()
    print(f"you entered - {lst_words} ")
    x=0

lst_words.sort()
print(f"words in sorted order- {lst_words} ") 

#-----------------------------------------------------------------------------------------
'''3. Write a program, which will find all the numbers between 1000 and 3000 (both
included) such that each digit of a number is an even number. The numbers
obtained should be printed in a comma-separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to
be a console input. Divide each digit with 2 and verify is it even or not'''

def checkAllEvenDig(num):
        str_num = str(num)

        for c in str_num:
            if int(c)%2 !=0:
                return False
        return True        

_lst_result=[]
counter=0

for i in range(1000,3001):
    x = checkAllEvenDig(i)
    if x==True:
        _lst_result.insert(counter,i) 
        counter+=1
print(f"List of number between 1000-3000 having all even digit is {_lst_result}")        


#-----------------------------------------------------------------------------------------
'''4. Write a program that accepts a sentence and calculates the number of letters
and digits.
Suppose if the entered string is: Python0325
Then the output will be:
LETTERS: 6
DIGITS:4
Hint: Use built-in functions of string.
'''
sentence=input("Write a sentence --> ")
str_words=sentence.split()
count_letters=0
count_digits=0

def count_Chars(str1):
    global count_letters
    global count_digits

    _digitflag= False
    _letterFlag= False

    for c in str1:
        _digitflag = c.isnumeric()
        _letterFlag = c.isalpha()
        if (_digitflag==True):
            count_digits+=1
        elif (_letterFlag==True):
            count_letters+=1
        else:
            continue

for wrd in str_words:
    count_Chars(wrd)

print(f"LETTERS:{count_letters}\nDIGITS:{count_digits}")

#-----------------------------------------------------------------------------------------
'''5. Design a code that will find whether the given number is a Palindrome number or
not.
Hint: Use built-in functions of string.
'''
str_num = input("Enter a numeric number --> ")
print(str_num)

if str_num.isnumeric():
   str_rev=reversed(str_num)
   str2=''.join(str_rev)
   if int(str2)==int(str_num):
       print("number is a palindromic number")    
   else:
       print("number is NOT a palindromic number")  


