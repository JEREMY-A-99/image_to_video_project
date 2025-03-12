'''
overlay text and transform image
'''

from PIL import Image, ImageDraw, ImageFont

def process_image(image_path, output_path, text):
    """
    Loads an image, applies a grayscale transformation, overlays text, and saves it.
    
    :param image_path: Path to the original image.
    :param output_path: Path to save the processed image.
    :param text: Text to overlay on the image.
    """
    try:
        image = Image.open(image_path)

        # Apply grayscale effect
        image = image.convert("L")

        # Overlay text on the image
        draw = ImageDraw.Draw(image)
        
        # Load a default font (change path if a specific font is needed)
        try:
            font = ImageFont.truetype("arial.ttf", 40)  # Windows
        except IOError:
            font = ImageFont.load_default()  # Fallback if font is unavailable

        # Define text position
        text_position = (50, 50)
        draw.text(text_position, text, fill="white", font=font)

        # Save the modified image
        image.save(output_path)
        print(f"Processed image saved at {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {e}")
