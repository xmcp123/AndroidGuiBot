import pyautogui
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
