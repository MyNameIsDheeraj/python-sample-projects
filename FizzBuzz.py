
# num = float(input("Enter a number for the FizzBuzz game "))
# num = 0
# while num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")

#     elif num % 3 == 0:
#         print("Fizz")

#     elif num % 5 == 0:
#         print("Buzz")

#     else:
#         print(f"The number {num} is not divisible bu 3 or 5")

#     num += 1


choose = int(input("Enter the range you want "))

def function(cho):
    for num in range(0,cho + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")

        else:
            print(f"The number {num} is not divisible by 3 or 5")

        num += 1

function(choose)