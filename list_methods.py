items=[ "apple ","banana","orange","pinapple"] #lenght of the list is calculated
print(len(items))

items.append("strawberries")        #add strawberries to the list 
print(items)

items.insert(1,"strawberries")      # add strawberries in index 1
print(items)

items.extend(["more bananas","chiku"])  #add
print(items) 

items.remove("banana")      # remove banana from the list 
print(items)

items.pop()                 #will remove last element from the list 
print(items)

items.pop(0)                  #index value 0 will be removed from the list 
print(items)

# #items.clear()                 #empty the list 
# #print(items)

print("index of pinapple :",items.index("pinapple"))  #index value of pinapple 


print("index of orange :",items.index("orange")) #index value of orange 

numbers=[11,2,4,3,0,67,87,9,1]       # sort numbers in acending order 
numbers.sort()
print(numbers)

numbers.sort(reverse=True)          #arrange numbers in decending order   
print(numbers)

print(11 in numbers)                 #if 11 is there in the list it will show True

print(11 not in numbers )