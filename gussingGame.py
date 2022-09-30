secret_word= "Mansour"

i=int(input("enter number of gusses: "))


def Gusesing(theWord,try_num):
    guess= ""

    while guess != theWord:
        
        print("number of tries: " + str(try_num))
        

        guess=input("\nenter guess: ")
        try_num-=1


        if guess==theWord:
            print("You WIN")
            break
        
        if try_num!=0:
            print("\nTry agine")
        if try_num==0:
            print("You LOSS")
            break  
        
print("Game started")       
Gusesing(secret_word,i)
