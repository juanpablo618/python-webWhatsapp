import webbrowser
import keyboard
import time

import csv
with open('whatsappPhone.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row[1])
csvFile.close()


webbrowser.open_new_tab('https://web.whatsapp.com/send?phone='+row[0]+'&text='+row[1])


print("apretando esc")
keyboard.press_and_release('esc')
print("ya apreto esc")


# https://web.whatsapp.com/send?phone=553513220999&text=oasdoasodas