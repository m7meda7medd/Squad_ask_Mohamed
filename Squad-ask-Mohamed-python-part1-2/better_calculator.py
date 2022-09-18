


# functions definations
def add(n1,n2) :
    return n1+n2
def subtract(n1,n2) :
    return n1-n2
def multiply (n1,n2) :
    return n1*n2
def divide(n1,n2) :
    return n1/n2 
def factorial(n) :
    result=1
    while n>0 :
        result*=n 
        n-=1  
    return result    
# the algorithm
while True :
    try :
        num1= float (input("The First number is :")) # taking num1 asfloat
        num2= float (input("The Second number is :"))#taking num2 as float          
        Operation = str(input("enter an operation from (+ , - , / , *,factorial) : ")) # taking operation as input string
        if   Operation == "+" :
            result=add(num1,num2)
        elif Operation == "-" :
            result=subtract(num1,num2)
        elif Operation == "*" :
            result=multiply(num1,num2)
        elif Operation == "/"  :
            if num2!=0 :
                result=divide(num1,num2)
            else :
                print ("can't divide by zero")   

        elif Operation == "factorial"  :
            n=int(input("enter the number to get it's factorial "))
            if n<=0 :
                print("invalid")
            else :
                result = factorial(n)    
        else :
            print("invalid operation try again")
            continue 

        print("the result of operation = ",result)  
    except :
        print("invalid input try again")

