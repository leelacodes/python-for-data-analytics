s1={1,2,4,6,7,8,9,7}
print(s1)

s2=set()         #empty set

#set doesnot maintain order 
items={"apple","banana"}
items.add("orange")
print(items)

items.update(["mango","peach"])
print(items)

items.remove("banana")
print(items)

items.discard("mangoe")       #if spell wrong no error will be shown 

items.pop()          #any raandom item will be removed 
print(items)

a=items.pop()       #the item which is remove will be shown 
print(items)
print(a)

print(len(items))

items.clear()
print(items)         #all item in the set will be removed 
