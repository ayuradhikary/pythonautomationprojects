
#        OverView :-

#ask time input from the user
#count downs start
#when the count down completes
#we create a sound.

from playsound import playsound
import time 

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0 #time passed

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1) #pauses for a second
        time_elapsed += 1 #increasing time passed by 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will start in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")


minutes = int(input("How many minutes to wait:"))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)


