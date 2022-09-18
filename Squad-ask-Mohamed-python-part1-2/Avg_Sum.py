try :
    num1,num2,num3 = list(map(float,input("enter the three numbers separated with spaces :").split())) #take the three  numbers separated with spaces
    sum = num1 + num2 + num3  # sum 
    Avg =sum/3 #sum/ 3 ==  Average
    print ("the sum is : %3.3f  "%sum) #print sum 
    print ("the Average is : %3.3f  "%Avg) #print average
except :
    print("invalid , please enter three numbers separated with spaces") #control the input     

