import datetime
import time
import winsound

def set_alarm(alarm_time):
    print(f" Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print(" Wake up! Alarm ringing...")
            for _ in range(10):
                winsound.Beep(1000, 1000)
            break
        time.sleep(30)  

if __name__ == "__main__":
    print(" Day 18 of #75DaysOfCode — Alarm Clock in Python")
    alarm_time = input("Enter alarm time (HH:MM in 24hr format): ").strip()
    set_alarm(alarm_time)


