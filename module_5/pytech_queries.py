"""System module."""

from pymongo import MongoClient

URL="mongodb+srv://admin:admin@cluster0.fwchebu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(URL)
db = client['pytech']
collection = db['students']

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for students in collection.find({},{"_id":0,"Student_ID":1,"First_Name":1,"Last_Name":1}):
    print("Student ID: ",students["Student_ID"])
    print("First Name: ",students["First_Name"])
    print("Last Name: ",students["Last_Name"])
    print("\n")

print("\n")

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
single_student = collection.find_one({"Student_ID":1009},{"_id":0,"Student_ID":1,"First_Name":1,
"Last_Name":1})
print("Student ID: ",single_student["Student_ID"])
print("First Name: ",single_student["First_Name"])
print("Last Name: ",single_student["Last_Name"])
print("\n")
