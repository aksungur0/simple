from libs.img_processor import process_image
from libs.validator import validate_input
from libs.logger import log_event
from libs.uploader import upload_image

def main():
    try:
        with open("input.png", "rb") as f:
            image_data = f.read()
    except FileNotFoundError:
        print("input.png not found.")
        return

    if validate_input(image_data):
        log_event("Input validated.")
        processed = process_image(image_data)
        upload_image(processed)
        log_event("Image processed and uploaded.")

if __name__ == "__main__":
    main()
