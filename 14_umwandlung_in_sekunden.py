
from datetime import datetime
user_input = input("Zeiteingabe im Format hh:mm:ss: ")
time_object = datetime.strptime(user_input,"%H:%M:%S")

seconds = 3600*time_object.hour + 60 * time_object.minute + time_object.second
print(f"Seconds: {seconds}")

