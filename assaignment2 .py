'''
#   Exception Handling
#  1. Syntax Errors
#  2. Runtime Error


# Eg 1: Syntax Errors
# x=1
# if x==1
#  print("where is colon")



# Eg 2:  runtime error
# def concat(a,b):
#     print(a+b)
# concat(10,'hai')    




try:
    f = (open('myfile','w'))
    a,b = [int(x) for x in input('enter the number :').split() ]
    c = a/b
    print('writing %d into myfile' %c)
except zeroDivisionError:
    print('Division by zero happened')
    print('please do not enter 0 in input')
finally:
    f.close()
    print('finally closed')
    
    
    
    #without try-except:
print("stmt-1") 
print(10/0) 
print("stmt-3") 




#with try-except:
print("stmt-1") 
try:
    print('stmt -4')
    print(10/0) 
    print('divisin by zero error')
except:    
    print("stmt-3") 
    
    
    
    try:
    print(10/0)
except ZeroDivisionError as msg: 
    print("exception raised and its description is:",msg)
    
    
    
    try: 
    x=int(input("Enter First Number: ")) 
    y=int(input("Enter Second Number: ")) 
    print(x/y) 
except (ZeroDivisionError,ValueError) as msg: 
    print("Plz Provide valid numbers only and problem is: ",msg) 
    
    
    
    #Case-1: If there is no exception
try: 
    print("try") 
except: 
    print("except") 
finally: 
    print("finally") 



#Case-2: If there is an exception raised but handled:
try: 
    print("try") 
    print(10/0) 
except ZeroDivisionError: 
    print("except") 
finally: 
    print("finally") 
    
    
    
    
    #  Note: There is only one situation where finally block won't be executed ie whenever we are using os._exit(0) function.
import 

try: 
    print("try") 
    os._exit(0) 
except NameError: 
    print("except") 
finally: 
    print("finally") 
    
    
    
    try: 
    print("outer try block") 
    try: 
        print("Inner try block") 
        print(10/0) 
    except ZeroDivisionError: 
        print("Inner except block") 
    finally: 
        print("Inner finally block") 
except: 
    print("outer except block") 
finally: 
    print("outer finally block") 
    
    
    
    
    
    
    try: 
    print('outer try block') 
    print(10/0)
    print('3rd outer')
    try: 
        print("Inner try block") 
        print(10/0) 
    except ZeroDivisionError: 
        print("Inner except block") 
    finally: 
        print("Inner finally block") 
except: 
    print("outer except block") 
finally: 
    print("outer finally block") 
    
    '''