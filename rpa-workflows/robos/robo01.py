from selenium import webdriver
import pyautogui
import time

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')

time.sleep(2)

pyautogui.write('Hello world', interval=0.1)

time.sleep(2)

pyautogui.hotkey('alt', 'f4')

time.sleep(1)

pyautogui.press('tab') 

time.sleep(1)

pyautogui.press('enter')