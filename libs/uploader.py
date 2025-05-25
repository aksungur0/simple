import os

def upload_image(image_data: bytes):
    try:
        with open("output.png", "wb") as f:
            f.write(image_data)
        print("Image saved as output.png")
    except Exception as e:
        print("Upload failed:", e)
