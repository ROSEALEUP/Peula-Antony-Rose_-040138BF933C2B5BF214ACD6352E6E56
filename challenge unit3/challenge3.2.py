class student:
 def __init__(self, name, roll_no, cgpa):
  self.name = name
  self.roll_no = roll_no
  self.cgpa = cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)

  return sorted_students

students=[student("student1","001",7.0),
        student("student2","002",8.0),
        student("student3","003",6.0),
        student("student4","004",9.0),
        student("student5","005",9.8),
         ]

sorted_students=sort_students(students)

for student in sorted_students:
  print("Name:{} Roll_no:{} CGPA:{}".format(student.name,student.roll_no,student.cgpa))  
