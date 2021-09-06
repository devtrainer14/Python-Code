'''
Created on May 3, 2019

@author: sipika
'''
winner_tickets=[]
num_on_ticket=[]
list2=[]
abc=0
total_num=int(input("Enter the number of test cases:- "))
if((total_num >= 1) and (total_num <= 10)):
    for i in range(0, total_num):
        num_houses=int(input("Enter the number of houses:- "))
        if((num_houses >= 1) and (num_houses <= 10000)):
            num_on_ticket=[]
            for j in range(0,num_houses):
                element=int(input("Enter the number on ticket:- "))
                if((element >= -1000) and (element<=1000)):
                    num_on_ticket.append(element)
            print(num_on_ticket)
        # print(b)

        for k in range(0,len(num_on_ticket)):
            c =(num_on_ticket[i-1] + num_on_ticket[i+1])
            for m in range(0,len(num_on_ticket)):
                if( c > num_on_ticket[m]):
                    abc = (str)(num_on_ticket[i-1])
                else:
                    pass
        list2.append(abc)
        print(list2)