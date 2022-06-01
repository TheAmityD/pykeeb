# PyKeeb

No, it's not a *mechanical keyboard* thing, it's just a typing bot I made in Python. I would do it in node.js but ehh  

## How to use

First of all you need to get dependencies of course...  

``pip install pytesseract pynput opencv-python pyautogui``  

And of course, install [Tesseract](https://tesseract-ocr.github.io/tessdoc/Downloads.html).  
Then on line 10 of ``keeb.py``, follow the instructions. For macOS and Linux and whatnot, I don't know where it is, can just send me PR lol.  
And finally on line 11, use [MouseLoc](https://www.softpedia.com/get/Desktop-Enhancements/Other-Desktop-Enhancements/MouseLoc.shtml#download) to grab two points, from the top left and the bottom right and put them in the numbers section of the line thing.  

``...region=(ax, ay, bx, by))``  

Then run the script. Ta-da!  
Please don't ask me if there's errors. e