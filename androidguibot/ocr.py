import pytesseract
from PIL import ImageEnhance
import PIL
import sys
def get_text_at_coordinates(img, top_left, bottom_right, clean_img=False, color=0, brightness=0.3, contrast=10, resize_factor=2):
    x1,y1 = top_left
    x2,y2=bottom_right
    im = img.copy()
    im = im.crop((x1,y1,x2,y2))
    return get_text_from_image(im, clean_img=clean_img, brightness=brightness, color=color, contrast=contrast, resize_factor=resize_factor)
def clean_text(img, color=0, brightness=0.3, contrast=10, resize_factor=2):
    img = img.convert('RGB')
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(color)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    w, h = img.size

    newsize = (w * resize_factor, h * resize_factor)
    img = img.resize(newsize)
    return img
def get_text_from_image(img, clean_img = False, brightness=0.3, color=0, contrast=10, resize_factor=2):
    im = img.copy()
    if clean_img:
        im = clean_text(im, color=color, brightness=brightness, contrast=contrast, resize_factor=resize_factor)
    text=pytesseract.image_to_string(im, config='--psm 10 --oem 3').strip()
    return text