from math import ceil

from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)

from pwn import *
import qrtools
from PIL import Image
from pyzbar.pyzbar import decode


PIL_GRAYSCALE = 'L'
PIL_WIDTH_INDEX = 0
PIL_HEIGHT_INDEX = 1
COMMON_MONO_FONT_FILENAMES = [
    'DejaVuSansMono.ttf',  # Linux
    'Consolas Mono.ttf',   # MacOS, I think
    'Consola.ttf',         # Windows, I think
]




def textfile_to_image(data):
    lines = tuple(data.splitlines())

    # choose a font (you can see more detail in the linked library on github)
    font = None
    large_font = 20  # get better resolution with larger size
    for font_filename in COMMON_MONO_FONT_FILENAMES:
        try:
            font = ImageFont.truetype(font_filename, size=large_font)
            break
        except IOError:
            print(f'Could not load font "{font_filename}".')
    if font is None:
        font = ImageFont.load_default()

    # make a sufficiently sized background image based on the combination of font and lines
    font_points_to_pixels = lambda pt: round(pt)
    margin_pixels = 0

    # height of the background image
    tallest_line = max(lines, key=lambda line: font.getsize(line)[PIL_HEIGHT_INDEX])
    max_line_height = font_points_to_pixels(font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
    realistic_line_height = max_line_height  # apparently it measures a lot of space above visible content
    image_height = int(ceil(realistic_line_height * len(lines)))

    # width of the background image
    widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
    max_line_width = font_points_to_pixels(font.getsize(widest_line)[PIL_WIDTH_INDEX])
    image_width = int(ceil(max_line_width))

    # draw the background
    background_color = 255  # white
    image = Image.new(PIL_GRAYSCALE, (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # draw each line of text
    font_color = 0  # black
    horizontal_position = margin_pixels
    for i, line in enumerate(lines):
        vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
        draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)

    return image



r = remote('125.235.240.166', 20123)
for i in range(100):
    try:
        print(r.recvuntil(':\n'))
        qr = r.recvuntil('ID Number: ').replace(b'ID Number: ', b'')
        image = textfile_to_image(qr.decode())
        image.save('content.png')



        qr = decode(Image.open('content.png'))[0]
        data = qr.data
        print(data)
        arr = data.split(b'|')
        print(arr)
        r.sendline(arr[0])
        r.recvuntil('Full Name: ')
        r.sendline(arr[1])
        r.recvuntil('Expired Date: ')
        r.sendline(arr[2])
    except Exception as e:
        print(e)
        pass
print(r.recv(10240))