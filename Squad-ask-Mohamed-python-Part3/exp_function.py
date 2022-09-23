def exponent_func(Number,Power) : #exponent function takes Positive and negative values of power and numbers
    result = 1  # put 1 to result  
    if Power >=0 :
        for i in range (Power) : # multiply by (power) times .. 
            result*=  Number
        return result 
    elif Power<0 :
       ResultNegative = 1/(exponent_func(Number,-Power))  # call the Exponent function with negative value of power -ve power =1/+ve power
       return ResultNegative      # return exponent with negative powers     



Num=int(input("Enter The number:"))  # take num and power
Power=int(input("enter the power:"))   
print("the result :",exponent_func(Num,Power)) 