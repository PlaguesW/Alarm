from datetime import datetime
from playsound import playsound


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Wrong format, please try again"
    else:
        if int(alarm_time[0:2]) > 23:
            return "Wrong hours format, please try again"
        elif int(alarm_time[3:5]) > 59:
            return "Wrong minutes format, please try again"
        elif int(alarm_time[6:8]) > 59:
            return "Wrong seconds format, please try again"
        else:
            return "Right"


while True: # Requesting the time to set an alarm
    alarm_time = input("Please enter the alarm time in format 'HH:MM:SS'\n Alarm time:")

    validate = validate_time(alarm_time) #Assign the result of the function
    if validate != "Right":
        print(validate)
    else:
        print(f"Alarm set on {alarm_time}...")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("Wakey-Wakey")
                #playsound()
                break