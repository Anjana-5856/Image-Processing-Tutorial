from PIL import Image, ImageEnhance
im= Image.open(r"E:\ImageProcessing\bob.png")
im3 = ImageEnhance.Brightness(im)
im3.enhance(2.0).show()