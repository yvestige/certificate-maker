import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# List of names and titles (Predefined inside the script)
PEOPLE = [
{"name": "Raymond F. Simbulan", "title":"REGIONAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Renato O. Datang", "title":"PROVINCIAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Evelinda S. De Guzman", "title":"MUNICIPAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Jennylyn T. Manalo", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Gemma S. Casem", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Winie M. Salunga", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Leticia S. Cordero", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Violeta J. Simbulan", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Carl A. Del Carmen", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Melodina S. Macasaquit", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Jenel L. Biag", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Carmelita M. Mendiola", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Lucila D. Toralles", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Edith M. Castro", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Adoracion D. Pascual", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Norma S. De Guzman", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Joselito B. Bodonia", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Nicole R. Evangelista", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Octavio C. Cruz Jr.", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "William T. Biag", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Karen C. Sales", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Florentino G. Calura Jr.", "title":"MUNICIPAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Annabeth B. Calura", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Jesus M. Carlos", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Nely C. Calura", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ray J. Pascua Jr.", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Danilo C. Angel", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Anita M. Lazarra", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ruben B. Damsai Sr.", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Bonifacio M. Capinpin", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Cresencia J. Pascua", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Arceli S. Manaois", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Melanio S. Novesteras", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Victoria M. Gado", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Myrna A. Capinpin", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Necitas C. Martin", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Teresita C. Martin", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Leonida C. Sapad", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Crisanto A. Facun", "title":"MUNICIPAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Gina Q. Facun", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Arceli P. Facun", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Dominador D. Tabaquero", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Tirso P. Bautista", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Rose Ann M. Bacsa", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "July P. Vergara", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Sandra B. Pascua", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Crestee C. Santos", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ariel E. Tababa", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Angelica M. Valentino", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Lorena T. Navarro", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Derik B. Dela Pasion", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Marilou B. Acosta", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Noriel G. Rodriguez", "title":"MUNICIPAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Divina V. Gamurot", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Matilde M. Taga", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Bernie A. Silvestre", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Jinky G. Agonoy", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ma. Theresita G. Evangelista", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Conchita B. Ragadio", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Imelda F. Casupanan", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Romana J. Lomboy", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Orlando O. Videz", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Milagros T. Gawat", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Adulia G. Gregorio", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Jessa Mae G. Lacsa", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Eloisa P. Ortis", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Wilson C. Mesa", "title":"MUNICIPAL ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Angelito O. Datang", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Edgar T. Baun", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Gener C. Laquindanum", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Purita G. Capulong", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ma. Jesusa A. Castro", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Kalvin G. Capulong", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Noel S. Bagain", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Feliciana O. Mesa", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Ma. Cristina S. Bautista", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
{"name": "Lolita C. Mateo", "title":"BARANGAY ADMINISTRATIVE OFFICER (Region III)"},
]

# Paths
TEMPLATE_PDF = "etc/certificate_template.pdf"  # Your original certificate template
NAME_FONT_PATH = "fonts/LucidaUnicodeCalligraphyBold.ttf"  # Font for Name
TITLE_FONT_PATH = "fonts/CormorantGaramond-Bold.ttf"  # Font for Title
OUTPUT_FOLDER = "output"  # Folder to store certificates
COMBINED_PDF = "certificates_combined.pdf"

# Font settings (separate for name and title)
NAME_FONT_SIZE = 41
TITLE_FONT_SIZE = 24
TEXT_COLOR = (0, 0, 0)  # Black

# Desired text center positions on the PDF
NAME_POSITION = (430, 183)   # (x, y) center position for name
TITLE_POSITION = (430, 267)  # (x, y) center position for title

# Image settings for overlay (adjust if needed)
IMG_WIDTH, IMG_HEIGHT = 1000, 500  

# Ensure necessary directories exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Ensure the font files exist
for font_path in [NAME_FONT_PATH, TITLE_FONT_PATH]:
    if not os.path.exists(font_path):
        print(f"Error: Font '{font_path}' not found! Place a valid TTF font in the folder.")
        exit(1)

# Store generated PDF paths for merging
generated_pdfs = []

# Process each person in the list
for person in PEOPLE:
    name = person["name"]
    title = person["title"]
    output_pdf = os.path.join(OUTPUT_FOLDER, f"certificate_{name.replace(' ', '_')}.pdf")
    generated_pdfs.append(output_pdf)

    # Create a transparent image for the text overlay
    img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Load fonts
    name_font = ImageFont.truetype(NAME_FONT_PATH, NAME_FONT_SIZE)
    title_font = ImageFont.truetype(TITLE_FONT_PATH, TITLE_FONT_SIZE)

    # Get text size for name
    name_bbox = draw.textbbox((0, 0), name, font=name_font)
    name_width, name_height = name_bbox[2] - name_bbox[0], name_bbox[3] - name_bbox[1]
    
    # Get text size for title
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width, title_height = title_bbox[2] - title_bbox[0], title_bbox[3] - title_bbox[1]

    # Compute the centered positions
    name_x = NAME_POSITION[0] - (name_width // 2)
    name_y = NAME_POSITION[1] - (name_height // 2)
    
    title_x = TITLE_POSITION[0] - (title_width // 2)
    title_y = TITLE_POSITION[1] - (title_height // 2)

    # Draw text onto the image
    draw.text((name_x, name_y), name, font=name_font, fill=TEXT_COLOR)
    draw.text((title_x, title_y), title, font=title_font, fill=TEXT_COLOR)

    # Save the overlay image
    overlay_path = "text_overlay.png"
    img.save(overlay_path)

    # Open the certificate template
    doc = fitz.open(TEMPLATE_PDF)
    page = doc[0]  # First page

    # Insert the overlay image into the PDF
    page.insert_image(fitz.Rect(0, 0, IMG_WIDTH, IMG_HEIGHT), filename=overlay_path)

    # Save the new certificate
    doc.save(output_pdf)
    doc.close()

    print(f"✅ Certificate generated: {output_pdf}")

# Merge all generated certificates into one PDF
if generated_pdfs:
    merged_doc = fitz.open()
    for pdf in generated_pdfs:
        merged_doc.insert_pdf(fitz.open(pdf))
    merged_doc.save(COMBINED_PDF)
    merged_doc.close()
    print(f"📄 Combined PDF created: {COMBINED_PDF}")

# Clean up temporary files
os.remove(overlay_path)