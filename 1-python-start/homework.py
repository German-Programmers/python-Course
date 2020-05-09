# >100 or <0   print error
# >=90  print Excellent
# [80 - 90[  print very good
# [70 - 80[ print good
# [60 - 70[ print middle
# [50 - 60[ print weak
# < 50 print Fail
grade = float(input("Enter the Grade "))
if grade > 100 or grade < 0:
    print("Error: grade out of range")
elif grade >= 90:
        print("Excellent")
elif grade >= 80:
    print("Very Good")
elif grade >= 70:
    print("good")
elif grade >= 60:
    print("middle")
elif grade >= 50:
    print("Weak")
else:
    print("Fail")