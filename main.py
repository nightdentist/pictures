from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")

red, green, blue  = rgb_image.split()

coordinates = (40, 0 , red.width, red.height)
cropped_red_left = red.crop(coordinates)

coordinates = (20, 0 , 676, red.height)
cropped_red_middle = red.crop(coordinates)

blend_red = Image.blend(cropped_red_left, cropped_red_middle, 0.5)


coordinates = (0, 0 , 656, blue.height)
cropped_blue_right = blue.crop(coordinates)

coordinates = (20, 0 , 676, blue.height)
cropped_blue_middle = blue.crop(coordinates)

blend_blue = Image.blend(cropped_blue_right, cropped_blue_middle, 0.5)

coordinates = (20, 0 , 676, green.height)
cropped_green_middle = green.crop(coordinates)

monro3 = Image.merge("RGB", (blend_red, cropped_green_middle, blend_blue))

monro3.thumbnail((80, 80))
print(monro3.size)
monro3.save("monro3.jpg")
