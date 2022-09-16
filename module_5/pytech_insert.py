"""System module."""

from pymongo import MongoClient

URL="mongodb+srv://admin:admin@cluster0.fwchebu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(URL)
db = client["pytech"]
collection = db["students"]

new_student_object = { "Student_ID": 1007, "First_Name": "Thorin", "Last_Name": "Oakenshield"}
new_student_object2 = { "Student_ID": 1008, "First_Name": "Bilbo", "Last_Name": "Baggins"}
new_student_object3 = { "Student_ID": 1009, "First_Name": "Frodo", "Last_Name": "Baggins"}

new_student_Id = collection.insert_one(new_student_object).inserted_id
new_student_Id2 = collection.insert_one(new_student_object2).inserted_id
new_student_Id3 = collection.insert_one(new_student_object3).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record Thorin Oakenshield into the students collection with document Id ",
new_student_Id)
print("Inserted student record Thorin Oakenshield into the students collection with document Id ",
new_student_Id2)
print("Inserted student record Thorin Oakenshield into the students collection with document Id ",
new_student_Id3)
