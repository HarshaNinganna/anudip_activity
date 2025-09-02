from PIL import Image, ImageDraw, ImageFont
import os

def text_to_handwriting(text, output_file="handwriting.png"):
    img = Image.new("RGB", (1000, 500), color="white")
    draw = ImageDraw.Draw(img)

    font_path = "C:/Users/HARSHA/Downloads/Handwritten.ttf"  # change path
    if not os.path.exists(font_path):
        font_path = "arial.ttf"  # fallback if font not found

    font = ImageFont.truetype(font_path, 40)
    draw.text((50, 100), text, fill="black", font=font)
    img.save(output_file)
    print(f" Handwritten text saved as {output_file}")

# Example
sample_text = """Dear Future Me, 
Keep coding, keep learning, 
and keep creating amazing things! """
text_to_handwriting(sample_text)
