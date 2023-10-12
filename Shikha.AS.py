#P1-Python file created
grades_per_student = {'Alex': 80, 'Bernard': 80, 'Carolyn': 84, 'Damian': 96, 'Elisabeth': 75, 'Frank': 83, 'Georges': 74, 'Henry': 79, 'Ian': 60, 'Julie': 70, 'Kate': 68, 'Lucy': 55, 'Mary': 88, 'Nancy': 77, 'Oliver': 80, 'Parker': 81, 'Quinn': 79, 'Ryan': 60, 'Sam': 57, 'Tom': 72, 'Ulysses': 56, 'Victoria': 77, 'Will': 75, 'Xavier': 75, 'Yelena': 97, 'Zoey': 73}

#P2-Empty list created
students_with_low_scores=[]

#P3-Iteration over grades_per_student dictionary
for key in grades_per_student:
    print(key)
for value in grades_per_student.values():
    print(value)
for item in grades_per_student.items():
    print(item)

#P4-Modified grade associated with each student by dividing by 10    
for key in grades_per_student:
    grades_per_student[key] = grades_per_student[key] / 10
    print(grades_per_student)

#P5-Students with score above 8
new_grades_per_student={}
for key, value in grades_per_student.items():
    if value>8:
        new_grades_per_student[key]=value
        print(new_grades_per_student)

#P6-Added to empty list for students with score equal or below 8        
new_grades_per_student2={}
for key, value in grades_per_student.items():
    if value<=8:
     
        students_with_low_scores.append(key)
print(students_with_low_scores)

#P7-Iteration & Printing of students_with_low_scores_
students_with_low_scores_dic= {}
for key in students_with_low_scores:
      if key in grades_per_student:
        students_with_low_scores_dic[key] = grades_per_student[key]
        
for key,value in students_with_low_scores_dic.items():
    print(f"{key}:{value}")



