import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 访问 JSON 数据
students = data['students']
print(students)

# 遍历学生列表
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

# 访问学生的成绩
for student in students:
    grades = student['grades']
    print(f"Name: {student['name']}, Math: {grades['math']}, Science: {grades['science']}")