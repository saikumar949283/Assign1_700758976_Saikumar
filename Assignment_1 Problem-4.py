#Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class


score = float(input("Enter the class score: "))
if score >= 90:
    print("A Grade")
elif score >= 80:
    print("B Grade")
elif score >= 70:
    print("C Grade")
elif score >= 60:
    print("D Grade")
else:
    print("F Grade")

