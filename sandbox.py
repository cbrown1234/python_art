from PIL import Image, ImageDraw

n, m = (800, 800)
im = Image.new('RGBA', (n, m), (255, 255, 255))

no_str = 10
for i in range(no_str):
    draw = ImageDraw.Draw(im)
    draw.text((n/2, m/2), f"   Hello World {i}", fill=(100, 100, 100))
    im = im.rotate(360/no_str)

im = im.crop((200, 200, 600, 600))
im.show()


