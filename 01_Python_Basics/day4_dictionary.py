#notes are in readme file

fruits={
    "Apple",
    "Banana",
    "Orange"
}
#add new item
fruits.add("Mango")
#check if item exists
print("Apple" in fruits) #true if something exists
print(fruits)

#Ways to remove an item
#1-remove an item
fruits.remove("Orange")
print(fruits)

#2-discard it (no error if item not found)
fruits.discard("Pineapple")
print(fruits)

#3-Clear the set
fruits.clear()  #removes everything
print(fruits)

#Dictionary

student = {
    "name": "Shamaim",
    "age": 21,
    "city": "Lahore"
}

print(student)

#Access values
print(student["name"])
print(student["age"])
print(student["city"])

#add new key 
student["grade"]="A"
print(student)

#keys
for key in student.keys():
    print(key)

#Access values
for value in student.values():
    print(value)

#access items
for key,value in student.items():
    print(key,value)

#enumerate
for index, item in enumerate(student.items()):
    print(index, item)

#remove a key 
student.pop("grade")
print(student)

