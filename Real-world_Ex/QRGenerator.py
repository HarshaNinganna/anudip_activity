import qrcode
import cv2
from pyzbar.pyzbar import decode

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f" QR Code generated and saved as {filename}")

def read_qr(filename):
    """Read and decode a QR code from an image file."""
    try:
        img = cv2.imread(filename)
        decoded_objects = decode(img)
        if decoded_objects:
            for obj in decoded_objects:
                print(f" QR Code Data: {obj.data.decode('utf-8')}")
        else:
            print(" No QR Code found in the image.")
    except Exception as e:
        print(f" Error reading QR code: {e}")

if __name__ == "__main__":
    print(" QR Code Generator & Reader — Day 17 of #75DaysOfCode")
    print("1. Generate QR Code")
    print("2. Read QR Code")
    
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        text = input("Enter text or URL to encode: ")
        filename = input("Enter filename to save (e.g., mycode.png): ").strip() or "qrcode.png"
        generate_qr(text, filename)
    elif choice == "2":
        filename = input("Enter QR code image filename: ").strip()
        read_qr(filename)
    else:
        print(" Invalid choice.")
