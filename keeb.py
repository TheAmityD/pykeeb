import pytesseract
import random
import time
import cv2
import pyautogui
from pynput.keyboard import Controller

time.sleep(5) # 5 seconds is plenty for the user to get ready

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Put your Tesseract file path here, Windows example
pyautogui.screenshot('hell.jpg', region=(11, 80, 920, 994))
img = cv2.imread("hell.jpg") # Yes, I named the file hell.jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
file = open("recognized.txt", "w+")
file.write("")
file.close()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    file = open("recognized.txt", "a")
    text = pytesseract.image_to_string(cropped)
    file.write(text)
    file.write("\n")
    file.close

line = "|"

keeb = Controller()
print(text)

for char in text:
    if char != line:
        t = random.uniform(0.6, 0.15) # Types like a human at a speed of 100 WPM
        keeb.press(char)
        keeb.release(char)
        time.sleep(t)
    elif char == line: # idk what that does
        keeb.press('I')
        keeb.release('I')
