from wand.image import Image

filename=''

#blurred images, no filenames
with Image(filename='') as img:
    with img.clone() as blurred:
        blurred.gaussian_blur(0,6)
        blurred.save(filename='')

