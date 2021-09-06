# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist1 = [10,20,30];
print ("Values before calling function: ", mylist1)
changeme( mylist1 );
print ("Values outside the function: ", mylist1)