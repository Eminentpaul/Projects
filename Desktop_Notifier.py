from plyer import notification
import time

def notifyMe(title, message):

    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\\PYTHON\\Projects\\images\\Aha-Soft-Large-Time-Time.ico",
        timeout = 10,
    )

while True:
    time.sleep(10)
    if __name__ == '__main__':
        notifyMe("Hey Paulinus, take a break", " You should follow the 2020 rules about screen")