from PIL import Image, ImageFont, ImageDraw

FONT_COLOR = (255, 245, 157)

template = Image.open("github_profile_scene_template.png")
heading_font = ImageFont.truetype('dpcomic/dpcomic.ttf', 100)
content_font = ImageFont.truetype('dpcomic/dpcomic.ttf', 60)

heading = "Hi! I'm Maxwell"
content = [
    "- I'm a CS undergraduate at New York University",
    "- I mostly code in Python, sometimes Javascript, C, Lua, or Go",
    "- I love reading books. Currently I'm reading:",
    "  Modern C",
    "  Microservices IN ACTION",
    "  The Writers Digest Handbook of Short Story Telling",
    "- Drop an issue here if you have any cool ideas you wanna share (or internship offers :-))"
]

image_editable = ImageDraw.Draw(template)
image_editable.text((80, 100), heading, FONT_COLOR, font=heading_font)
for i in range(len(content)):
    image_editable.text(
        (80, 240 + i*80),
        content[i],
        FONT_COLOR,
        font=content_font
    )

template.save("github_profile_scene.png")