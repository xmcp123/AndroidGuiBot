# Android GUI Bot

Control android emulator via normal screenshots and mouse/keyboard(PyAutoGui), or ADB shell commands. Basic OCR via PyTesseract.
Ideal if you are transitioning a project from one method to the other.


## Basic Setup
1) Start emulator
2) Start ADB and confirm device is visible
3) Make sure your PyTesseract directories are set(like in example.py).
4) That's about it. Most functions remain the same as PyAutoGui, aside from some commonly used botting functions and OCR/OCR cleaning functions.

## Example Setup

```commandline
import os
os.environ['TESSDATA_PREFIX'] = '''C:\\Program Files\\Tesseract-OCR\\tessdata'''
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


from androidguibot import AndroidGuiBot

if __name__ == "__main__":
    bot = AndroidGuiBot(adb_ip="127.0.0.1", adb_port=5037, use_adb=True)
    print("Connected")
    c = bot.get_controller()
    print("Text: {}".format(c.text_at_coordinate((143,83),(269,110), clean_img=True))) # print text at coordinates

```
