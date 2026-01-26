# methods of dictionary

student={
    "name":"leela",
    "city":"delhi",
    "company":"google"
}
print (student)

student.pop("name")    #remove name from dictionary
print(student)

student["class"]="12th"     #add class to the dictionary
print(student)

student.popitem()
print(student)          #last inserted key will be deleted

del student["city"]      #city will be deleted  
print(student)

print(student.values)
print(student)

print(student.items())
print(student)

print(student.keys())

print(student.clear())   #everything will be removed 
