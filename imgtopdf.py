from PIL import Image

def convert_to_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    img.convert('RGB').save(pdf_path)

convert_to_pdf("example.jpg", "output.pdf")
print("PDF created successfully!")


