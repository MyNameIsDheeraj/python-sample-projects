
score = float(input("Enter Youre Score "))

if score > 100:
    score = float(input("Please Enter a valid score "))

elif score < 60:
    print("Youre Failed....!")

elif score == 100:
    print("Youre grade is: A+")

elif str(score).startswith("9"):
    print("Youre great is: A+")

elif str(score).startswith("8"):
    print("Youre greade is: A")

elif str(score).startswith("7"):
    print("Youre gread is: B+")

elif str(score).startswith("6"):
    print("Youre grade is: B")


else:
    print("Youre Failed....!")