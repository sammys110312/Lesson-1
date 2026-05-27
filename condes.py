class Employee:
    def __init__(self):
        print("Object created")
    def __del__(self):
        print("Object destroyed")
s1 = Employee()
del s1