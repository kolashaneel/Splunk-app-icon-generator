from PIL import Image

image_path=str(input("Enter your icon or logo path for splunk icon generation : "))
try:
    image = Image.open(image_path)
except:
    print("invalid path")
    exit()

width,height=image.size

iconsizes={
    "appIcon_2x":(72,72),
    "appIcon":(36,36),
    "appIconAlt_2x":(72,72),
    "appIconAlt":(36,36),
    "appLogo":(160,40),
    "appLogo_2x":(320,80)
    }

for i in iconsizes:
    i_resized=image.resize(iconsizes.get(i))
    i_resized.save('{}.png'.format(i),optimize=True, quality=50)
    print('generated {}.png'.format(i))