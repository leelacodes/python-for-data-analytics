student={
    "name" : "leela",
    "city" : "delhi",
    "company" : "google"
}
print(student)

print(student["company"])
print(student["city"])

#print(student["nameee"])      #it will show error

print(student.get("nameeee"))

print(student.get("name"))

#add and update 
student["city"]="ghaziabad"
print(student)