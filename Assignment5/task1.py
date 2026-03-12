student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88
}
name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
