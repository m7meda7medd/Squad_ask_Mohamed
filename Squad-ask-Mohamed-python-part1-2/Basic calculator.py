num1= float (input("The First number is :")) # taking num1 asfloat
num2= float (input("The Second number is :"))#taking num2 as float


Operation = str(input("enter an operation from (+ , - , / , * ) : ")) # taking operation as input string

result = 0

if   Operation == "+" :
    result = num1+num2 
elif Operation == "-" :
    result = num1-num2
elif Operation == "*" :
    result = num1*num2 
elif Operation == "/"  :
    result=num1/num2 
else :
    print("invalid operation")

print("the result = ",result)        



