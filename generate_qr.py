import qrcode
from PIL import Image

# The URL for the GitHub Pages site
url = "https://coffeelike5282.github.io/Essence-Coffee-Manual/"

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for better scanning
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("essence-manual-qr.png")

print(f"QR Code generated for: {url}")
print("Saved as: essence-manual-qr.png")
