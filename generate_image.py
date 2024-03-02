from PIL import Image, ImageDraw, ImageFont


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height


def create_image(name, design):
    font_size = 180

    font_type = ImageFont.truetype("fonts/ofont.ru_Appetite.ttf", font_size)

    if design == "design_1":
        image = Image.open("images/1.jpg")
        color = "#7fe0f2"
        x = (image.width - textsize(name, font_type)[0]) / 2.1
        xy = (x, 2900.28)

    elif design == "design_2":
        image = Image.open("images/2.jpg")
        color = "#ffffff"
        x = (image.width - textsize(name, font_type)[0]) / 2.1
        xy = (x, 3180.28)

    elif design == "design_3":
        image = Image.open("images/3.jpg")
        color = "#294877"
        x = (image.width - textsize(name, font_type)[0]) / 4.4
        xy = (x, 1730.28)

    draw = ImageDraw.Draw(image)

    draw.text(xy=xy, text=name.title(), font=font_type, fill=color, align="center")

    image.save(f"{name}.jpg")


if __name__ == "__main__":
    create_image("John Doe", "design_3")
