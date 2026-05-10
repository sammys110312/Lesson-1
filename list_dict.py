student = [
    (1, "Sammy", 9),
    (2, "Aarush", 8),
    (3, "Adi", 7),
    (4, "Sparsh", 8),
    (5, "Jishnu", 10)
]

student_dict = {}

for schl in student:
    number = schl[0]

    student_dict[number] = {
        "Name" : schl[1],
        "Year" : schl[2]
    }

print(student_dict)