import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# List of names and titles (Predefined inside the script)
PEOPLE = [
    {"name": "John Doe", "title": "Certified Engineer"}
]

# Paths
TEMPLATE_PDF = "certificate_template.pdf"  # Your original certificate template
FONT_PATH = "LucidaUnicodeCalligraphyBold.ttf"  # Stylish font (Ensure it's in the same directory)
FONT_SIZE = 72
TEXT_COLOR = (0, 0, 0)  # Black
TEXT_POSITION = (0, 0)  # (x, y) Adjust to fit your template

# Image settings for overlay
IMG_WIDTH, IMG_HEIGHT = 1000, 300

# Ensure the font file exists
if not os.path.exists(FONT_PATH):
    print(f"Error: Font '{FONT_PATH}' not found! Place a valid TTF font in the folder.")
    exit(1)

# Process each person in the list
for person in PEOPLE:
    name = person["name"]
    title = person["title"]

    # Create a unique filename for each certificate
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # output_pdf = f"certificate_{name.replace(' ', '_')}_{timestamp}.pdf"
    output_pdf = f"certificate_{name.replace(' ', '_')}_.pdf"

    # Create a transparent image with the name and title
    img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Format text
    text = f"{name}\n{title}"
    
    # FIXED: Get text size using textbbox() instead of deprecated textsize()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Center the text
    x = (IMG_WIDTH - text_width) // 2
    y = (IMG_HEIGHT - text_height) // 2

    # Draw text onto the image
    draw.text((x, y), text, font=font, fill=TEXT_COLOR)

    # Save the overlay image
    overlay_path = "text_overlay.png"
    img.save(overlay_path)

    # Open the certificate template
    doc = fitz.open(TEMPLATE_PDF)
    page = doc[0]  # First page

    # Insert the overlay image into the PDF
    pos_x, pos_y = TEXT_POSITION
    overlay_img = fitz.open(overlay_path)
    page.insert_image(fitz.Rect(pos_x, pos_y, pos_x + IMG_WIDTH, pos_y + IMG_HEIGHT), filename=overlay_path)

    # Save the new certificate
    doc.save(output_pdf)
    doc.close()

    print(f"✅ Certificate generated: {output_pdf}")

# Clean up temporary files
os.remove(overlay_path)
