number_list= ["0505"]

i=int(input("how many number you want to add? "))






def addNum(rep):
    remark=1
    
    while remark<=rep:
        new_mumber=input("add new number: ")
        number_list.append(new_mumber)
        remark+=1
    print(number_list)

print(addNum(i))

print("the loop has ended")