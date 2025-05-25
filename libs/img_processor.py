from PIL import Image
import io

def process_image(image_data: bytes) -> bytes:
    try:
        image = Image.open(io.BytesIO(image_data))
        image = image.convert("L")  # Grayscale
        output = io.BytesIO()
        image.save(output, format="PNG")
        return output.getvalue()
    except Exception as e:
        print("Image processing failed:", e)
        return b''
