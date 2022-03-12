from PIL import Image, ImageDraw
import random
import requests
import json

nft_number = 15

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_nft(nft_name):
    img_size = 128
    padding_px = 16
    image_bg_col = random_color()
    thickness = 3

    image = Image.new("RGB", 
        size = (img_size, img_size), 
        color = image_bg_col)

    draw = ImageDraw.Draw(image)

    points = []
    for _ in range(3):
        random_point = (
            random.randint(padding_px, img_size-padding_px), 
            random.randint(padding_px, img_size-padding_px)
            )
        points.append(random_point)
        

    for i, point in enumerate(points):
        p1 = point
        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i+1]

        line_xy = (p1, p2)
        line_color = random_color()

        draw.line(line_xy, fill=(line_color), width=thickness)

    image.save(nft_name)


words = requests.get('https://random-word-api.herokuapp.com/word?number={}&swear=0'.format(str(nft_number)))
json_data = json.loads(words.text)

for name in json_data:
    generate_nft(name+'.png')
    
