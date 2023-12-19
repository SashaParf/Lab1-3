import time
from pywinauto.application import Application
import keyboard

app = Application().start("C:\Program Files\PuTTY\putty.exe -ssh sashaparfe@tty.sdf.org")

time.sleep(5)
keyboard.write("5UzmZqKm7mapig")


time.sleep(5)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(10)
