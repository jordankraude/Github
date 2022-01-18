from PIL import Image

# Resizing the PNG
img = Image.open(r"C:\Users\Jordan\Desktop\Downloaded Icons\6-2-youtube-png-picture.png")
resized_img = img.resize((200,200))
resized_img.save("resized_image.png")
