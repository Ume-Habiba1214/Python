results = {
    "Ali": 45, "Sara": 78, "Omar": 90, "Hina": 33,
    "Bilal": 67, "Zara": 88, "Usman": 52, "Ayesha": 19
}

for key,value in results.items():
    print(f"{key}: {value}")


max_value=-1
for key, value in results.items():
    if max_value<value:
        max_value=value
        max_key=key
print(f" {max_key}: {max_value} ")


pass_students={}
for name,marks in results.items():
    if marks>=50:
        pass_students[name]= marks

print(pass_students)



student_name=input("Enter the name of student: ")
print(results.get(student_name.strip().title(),"Student is not found"))