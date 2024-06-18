"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_info={'student_name':'prasad','age':22,'roll_no':72,'class':'B.tech','section':'a','percentage':75,'college_name':'JNTUA'}
print("percentage:",student_info['percentage'])

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
students_info = {'student_names': ['prasad', 'akil', 'pavan'], 'ages': [22, 23, 21],
                 'roll_nos': (21, 22, 25), 'classes': ['B.tech', 'M.tech', 'Degree'],
                 'sections': ['A', 'B', 'C'], 'percentages': [75, 78, 70]
                 }
print("student_3:",students_info['classes'][2])

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees={'employee1':{'employee1_name':'prasad','salary':25000,'designation':'Associate-3'},
           'employee2':{'employee2_name':'vishnu','salary':26000,'designation':'Associate-4'},
           'employee3':{'employee3_name':'akil','salary':27000,'designation':'Associate-1'},
           'employee4':{'employee4_name':'pavan','salary':28000,'designation':'Associate-2'}
         }

print("3rd employee Designation:",employees['employee3']['designation'])
