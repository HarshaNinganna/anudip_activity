from datetime import datetime

current_time = datetime.now()
current_hour = current_time.hour

if current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"{greeting}!")
