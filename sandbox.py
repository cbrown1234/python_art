from PIL import Image, ImageDraw, ImageFont

from query_twitter import get_tweet_text


def make_list_art(phrases):
    no_str = len(phrases)
    n, m = (800, 800)
    opacity = 150

    # get a font
    fnt = ImageFont.truetype('font/Amatic-Bold.ttf', 20)

    im = Image.new('RGBA', (n, m), (255, 255, 255))

    for i, phrase in enumerate(phrases):

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', im.size, (255, 255, 255, 0))

        # get a drawing context
        draw = ImageDraw.Draw(txt)

        draw.text(
            (n/2, m/2),
            phrase,
            fill=(0, 51, 102, opacity),
            font=fnt,
        )
        txt = txt.rotate(360*i/no_str)

        im = Image.alpha_composite(im, txt)
    return im


list_of_strings = get_tweet_text(screen_name='UniOfSurrey')

latin1_list = [
    tweet.encode("latin-1", "ignore").decode("latin-1")
    for tweet in list_of_strings
]

art = make_list_art(latin1_list)
art.show()
