

Secret_Word = "green" #secret word
guess = "" #empty guess :D
attempts = 3  #3 attempts only
while attempts : # while attempts not equal zero 
    if input("guess the secret word:").lower() == Secret_Word : #take lower case word and compare with secret word
        print("Right !! You Won ")  # if yes 
        break  # get out
    else :
        attempts-=1
        if attempts ==0 :
            print("Wrong !! You Lost ") # if no attempts
        else:
            print("wrong answer try again ,%d attempts left"%attempts)
