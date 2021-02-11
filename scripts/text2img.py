
# source: https://pythonprogramming.altervista.org/make-an-image-with-text-with-python/
from PIL import Image, ImageDraw, ImageFont
import os


def text_on_img(filename='../data/avatars/01.png', text="Hello", size=10, color=(255, 255, 0), bg='white'):
    "Draw a text on an Image, saves it, show it"
    font = ImageFont.truetype('../arial.ttf', size)
    # create image
    image = Image.new(mode="RGB", size = (3*int(size / 4) * len(text), size + 50), color=bg)
    draw = ImageDraw.Draw(image)
    # draw text
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))
    # save file
    image.save(filename)

input_txt = "RB"
fname = '../data/avatars/'+input_txt.lower()+'.png'
text_on_img(filename=fname,text=input_txt, size=300, bg='white')