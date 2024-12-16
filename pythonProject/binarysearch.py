import csv


def Calculate_grade(marks):
    if 0 <= marks < 40:
        return 'E'
    elif 40 <= marks < 50:
        return 'D'
    elif 50 <= marks < 60:
        return 'C'
    elif 60 <= marks < 70:
        return 'B'
    elif 70 <= marks <= 100:
        return 'A'
    else:
        return 'Invalid Marks'


def Calculate_average_and_grade(marks_list):
    average_marks = sum(marks_list) / len(marks_list)
    average_grade = Calculate_grade(average_marks)
    return average_marks, average_grade


def main():
    student_name = input("Enter the student's name: ")
    registration_number = input("Enter the student's registration number: ")



units = []
marks = []
grades = []

for i in range(1, 4):
    unit_name = input(f"Enter the name of unit {i}: ")
    unit_marks = int(input(f"Enter the marks for {unit_name}: "))

    units.append(unit_name)
    marks.append(unit_marks)
    grades.append(Calculate_grade(unit_marks))

average_marks, average_grade = Calculate_average_and_grade(marks)

csv_data = [
    ["Student Name", student_name],
    ["Registration Number", registration_number]
]
for i in range(3):
    csv_data.append([units[i], grades[i]])
csv_data.append(["Average Marks", average_marks, average_grade])

# Write to CSV file
csv_filename = f"{student_name}_grades.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print(f"\nStudent details and grades have been saved to {csv_filename}")

if __name__ == "__main__":
    main()





