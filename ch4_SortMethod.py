students = ["rom","Paul", "Alice", "Bob", "Charlie", "David"]
students.sort()
print(students)

# students.sort(reverse=True) modifies the original list

sorted_students = sorted(students)
print(sorted_students)

sorted_students_desc = sorted(students, reverse=True)
print(sorted_students_desc)

print(f"Student in sorted order :")

for student in students:
    print(f"student: {student}")