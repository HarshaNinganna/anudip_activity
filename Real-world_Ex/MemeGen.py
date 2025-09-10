from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_meme(image_path, top_text="", bottom_text="", output_path="meme_output.png"):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load font (download a bold font like Impact for memes)
    font = ImageFont.truetype("impact.ttf", size=int(height/10))

    # Function to draw text with outline
    def draw_text(text, position):
        lines = textwrap.wrap(text, width=15)
        y_text = position
        for line in lines:
            line_width, line_height = draw.textsize(line, font=font)
            x_text = (width - line_width) / 2
            # Draw outline
            draw.text((x_text-2, y_text-2), line, font=font, fill="black")
            draw.text((x_text+2, y_text-2), line, font=font, fill="black")
            draw.text((x_text-2, y_text+2), line, font=font, fill="black")
            draw.text((x_text+2, y_text+2), line, font=font, fill="black")
            # Draw main text
            draw.text((x_text, y_text), line, font=font, fill="white")
            y_text += line_height

    # Draw top and bottom text
    if top_text:
        draw_text(top_text, 10)
    if bottom_text:
        draw_text(bottom_text, height - int(height/4))

    # Save the meme
    img.save(output_path)
    print(f" Meme saved as {output_path}")

# Example usage
create_meme("example_image.jpg", top_text="When you code all night", bottom_text="And it finally works!")
