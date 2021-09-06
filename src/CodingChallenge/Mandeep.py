'''
Created on May 3, 2019

@author: sipika
'''
list2=[]

# def check(num_on_ticket,num_houses):
#     # self.num_on_ticket = num_on_ticket
    
#     for i in range(1, num_houses-1):
#         c=num_on_ticket[i-1]+num_on_ticket[i+1]
#         if(c < num_on_ticket[i]):
#             abc = c
#             print(abc)
#             # break
#         winner_tickets.append(c)
#     print(winner_tickets)
#     return abc

winner_tickets=[]
abc = 0
# num_on_ticket=[]
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
            for i in range(1, num_houses-2):
                c=num_on_ticket[i]+num_on_ticket[i+2]
                for m in num_on_ticket:
                    if(c > m):
                        abc = (str) (num_on_ticket[i])
                        abc1 = (str) (num_on_ticket[i+2])
                    # print(abc)
            # break
                    winner_tickets.append(abc + " "+ abc1)
                    print(winner_tickets)
                    # winner_tickets.sort()
                # for i in winner_tickets:
                    # bcs = winner_tickets[0]
                    # print(bcs)
        # b=check(num_on_ticket,num_houses)
        # print(b)
        # print(abc)
         # winner_tickets.sort()
         # abc.append

print(winner_tickets)
# print(list2)

