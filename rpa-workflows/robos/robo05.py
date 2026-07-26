import pyautogui as p
import time

p.hotkey('win', 'r')
time.sleep(1)
p.write('C:\RPA.pbix')
time.sleep(1)
p.press('enter')
p.sleep(25)
p.click(x=606, y=93)
p.sleep(12)
p.moveTo(x=1893, y=21, duration=1)
p.click()
p.moveTo(x=932, y=574, duration=1)
p.click()

#p.sleep(3)
# print(p.position())