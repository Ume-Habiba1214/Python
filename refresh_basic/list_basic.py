marks = [45, 78, 90, 33, 67, 88, 52, 99]

# average
total = 0
no_of_student = len(marks)
for mark in marks:
    total += mark
# secon way :  total=sum(marks)
average = total/no_of_student
print(f" Average Marks is {round(average,2)}.") 




# Lowest and Highest Marks
lowest_marks = min(marks)
highest_marks = max(marks)
print(f" Lowest Marks is {lowest_marks}. ")
print(f" Highest Marks is {highest_marks}. ")




# passing marks and sort the passing marks 
passed_marks = []
for mark in marks:
    if mark >= 50:
        passed_marks.append(mark)


no_of_passed = len(passed_marks)

print(f" Number of Passing Students are {no_of_passed}.")
sorted_marks = sorted(passed_marks, reverse=True)
print(f"List of Passed Marks = {passed_marks}")
print(f"Descending List of Passed Marks = {sorted_marks}")