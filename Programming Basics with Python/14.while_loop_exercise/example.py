from plyer import notification  # pip install plyer
from time import sleep

task_to_do = input("Enter the task: ")
show_after_seconds = int(input("Set the timer to (seconds): "))
# TODO: Let the user choose hours, minutes or seconds, make validations

sleep(show_after_seconds)  # accepts seconds

notification.notify(
    title="Remainder",
    message=task_to_do,
    app_icon="icon.ico",  # .ico for Windows, .png for linux
)
