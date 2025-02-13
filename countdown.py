import re
import time


count_time = input("Enter the time in minutes (Eg: 00:00) \n")

def check_time(count_time):
    pattern = r"^\d{1,2}:\d{2}$"
    if re.match(pattern, count_time):
        return True
    else:
        return False

while not check_time(count_time):
    count_time = input("Invalid input. Please enter the time in minutes (Eg: 00:00) \n")

def countdown_time(count_time):
    minutes, second = map(int, count_time.split(":"))
    total_seconds = minutes * 60 + second

    while total_seconds > 0:
        minutes_left = total_seconds // 60
        second_left = total_seconds % 60
        time_left = f"{minutes_left:02}:{second_left:02}"
        print(time_left, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("00:00")
    print("Time's up!")

countdown_time(count_time)
