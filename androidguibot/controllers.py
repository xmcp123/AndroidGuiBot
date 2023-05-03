import random
from random import randint
import os
import time
import pyautogui
from ppadb.client import Client as AdbClient
import io
from PIL import Image
import androidguibot.ocr as ocr
import sys
import pyscreeze


class AndroidController(object):
    def sleep_range(self, min_ms=1000, max_ms=2000):
        time.sleep(randint(min_ms, max_ms) / 1000)


class ADBAndroidController(AndroidController):
    def __init__(self, adb_ip, adb_port, device_index=0):
        self.adb_ip = adb_ip
        self.adb_port = adb_port
        self.adb_conn = None
        if not adb_ip:
            self.device = None  # Not implemented
        else:
            self.adb_conn = AdbClient(adb_ip, port=adb_port)
            self.device = self.adb_conn.devices()[device_index]

    def type(self, text):
        self.execute("input text {}".format(text))

    def type_slow(self, text):
        for letter in text:
            self.execute("input text {}".format(letter))

    def execute(self, command, timeout=5):
        return self.device.shell(command)

    def click_image(self, image, **kwargs):
        img = self.locateOnScreen(image, **kwargs)
        x, y, x2, y2 = img.left, img.top, img.left + img.width, img.top + img.height
        return self.click_inside(x, y, x2, y2)

    def click_inside(self, x, y, max_x=None, max_y=None):
        max_x = x if max_x is None else max_x
        max_y = y if max_y is None else max_y
        return self.execute(
            "input tap {} {}".format(randint(x, max_x), randint(y, max_y))
        )

    def drag(self, top_left, bottom_right, ms=500):
        x1, y1 = top_left
        x2, y2 = bottom_right
        return self.execute("input swipe {} {} {} {} {}".format(x1, y1, x2, y2, ms))

    def screenshot(self):
        data = self.device.screencap()
        img = Image.open(io.BytesIO(data))
        return img

    def locateAllOnScreen(self, image, **kwargs):
        return pyautogui.locateAll(image, self.screenshot(), **kwargs)

    def locateOnScreen(self, needleImage,  **kwargs):
        return pyautogui.locate(needleImage, self.screenshot(), **kwargs)

    def text_at_coordinate(self, top_left, bottom_right,clean_img = False, brightness=2, color=0, contrast=7, resize_factor=1):
        img = self.screenshot()
        return ocr.get_text_at_coordinates(img, top_left=top_left, bottom_right=bottom_right, clean_img=clean_img, brightness=brightness, color=color, contrast=contrast, resize_factor=resize_factor)
class EmulatorController(AndroidController):
    def __init__(self):
        self.__getattr_orig__ = self.__getattr__

    def __getattr__(self, item):
        """
        Forward all function calls pyautogui
        :param item: Attribute name
        :return: Attribute
        """
        if hasattr(pyautogui, item):
            return pyautogui.__getattribute__(item)
        else:
            return self.__getattr_orig__(item)

    def click_inside(self, x, y, max_x=None, max_y=None):
        """
        Click inside a given coordinate range
        :param x: left coord minimum
        :param y: y coord minimum
        :param max_x: max x minimum
        :param max_y: max y minimum
        :return:
        """
        return pyautogui.click(randint(x, max_x), randint(y, max_y))
    def text_at_coordinate(self, top_left, bottom_right,clean_img = False, brightness=0, color=0, contrast=0, resize_factor=2):
        img = self.screenshot()
        return ocr.get_text_at_coordinates(img, top_left, bottom_right, clean_img=clean_img, brightness=brightness, color=color, contrast=contrast, resize_factor=resize_factor)

