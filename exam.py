absent = int(input("How many days of school have you been absent from?: "))
working = int(input("How many school days do you have?: "))
eligibility = absent/working
percent1 = eligibility * 100
percent = 100-percent1
print(percent,"%")
if percent >= 75:
    print("Due to your high attendance percentage, we are excited to say that you can take part in the exam")
else:
    print("Unfortunately we are unable to let you into the exam due to your attendance")