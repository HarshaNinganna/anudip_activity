import time
import winsound

def countdown_timer(seconds):
    print(f" Timer set for {seconds} seconds\n")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r") 
        time.sleep(1)
        seconds -= 1
    print(" Time's up!")
    winsound.Beep(1000, 1000)  

def set_reminders():
    reminders = []
    count = int(input("How many reminders do you want to set? "))
    for i in range(count):
        mins = int(input(f"Enter duration for reminder {i+1} (in minutes): "))
        reminders.append(mins * 60)

    for idx, reminder in enumerate(reminders, start=1):
        print(f"\n Starting Reminder {idx}")
        countdown_timer(reminder)

if __name__ == "__main__":
    print("Day 23 of #75DaysOfCode — Countdown Timer with Reminders ")
    set_reminders()
