from PIL import Image


red = Image.open("red.jpg")
green = Image.open("green.jpg")
blue = Image.open("blue.jpg")

coordinates = (40, 0 , red.width, red.height)
cropped_red_left = red.crop(coordinates)
cropped_red_left.save("cropped_red_left.jpg")

coordinates = (20, 0 , 676, red.height)
cropped_red_middle = red.crop(coordinates)
cropped_red_middle.save("cropped_red_middle.jpg")

cropped_red_left = Image.open("cropped_red_left.jpg")
cropped_red_middle = Image.open("cropped_red_middle.jpg")

blend_red = Image.blend(cropped_red_left, cropped_red_middle, 0.5)
blend_red.save("blend_red.jpg")


coordinates = (0, 0 , 656, blue.height)
cropped_blue_right = blue.crop(coordinates)
cropped_blue_right.save("cropped_blue_right.jpg")

coordinates = (20, 0 , 676, blue.height)
cropped_blue_middle = blue.crop(coordinates)
cropped_blue_middle.save("cropped_blue_middle.jpg")

cropped_blue_right = Image.open("cropped_blue_right.jpg")
cropped_blue_middle = Image.open("cropped_blue_middle.jpg")

blend_blue = Image.blend(cropped_blue_right, cropped_blue_middle, 0.5)
blend_blue.save("blend_blue.jpg")

coordinates = (20, 0 , 676, green.height)
cropped_green_middle = green.crop(coordinates)
cropped_green_middle.save("cropped_green_middle.jpg")

monro3 = Image.merge("RGB", (blend_red, cropped_green_middle, blend_blue))
monro3.save("monro3.jpg")

avatar = Image.open("monro3.jpg")
avatar.thumbnail((80, 80))  # Картинка теперь размера 400 на 600
print(avatar.size)  # Вывелось (400, 600)
avatar.save("avatar.jpg")
