from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Example image (URL or local file)
image_url = "https://images.unsplash.com/photo-1602524202136-146a4d3a1f96"
image = Image.open(requests.get(image_url, stream=True).raw)

# Preprocess and generate caption
inputs = processor(images=image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print("️ Image Caption:", caption)
