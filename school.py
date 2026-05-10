student_details = {
    "Name" : "Sammy",
    "Age" : 14,
    "School" : "Reading School",
    "Town" : "Reading",
    "Year" : "Year 9"
}

print(student_details)
print(student_details["Name"])
student_details["Country"] = "England"
print(student_details)
student_details["Year"] = "Year 10"
print(student_details)
student_details.pop("Age")
print(student_details)
print(student_details.keys())
print(student_details.values())