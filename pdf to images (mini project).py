
import os
import img2pdf

image_folder = "C:\\Users\\Andrew\\Desktop\\toimages"
image_files = [os.path.join(image_folder, i) for i in os.listdir(image_folder) if i.endswith(".jpg")]

with open("ImageContainingBook.pdf", "wb") as file:
    image_bytes = [open(image, "rb").read() for image in image_files]
    file.write(img2pdf.convert(image_bytes))

