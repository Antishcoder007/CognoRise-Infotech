import qrcode 
import cv2
from pyzbar.pyzbar import decode

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def decode_qr(filename):
    img = cv2.imread(filename)
    decoded_objects = decode(img)
    if decoded_objects:
        for obj in decoded_objects:
            print("Data:", obj.data.decode('utf-8'))
    else:
        print("No QR code found in the image.")

def QrCode():
    while True:
        print("QR Code Encoder/Decoder")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            data = input("Enter the data to encode in the QR code: ")
            filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")
            generate_qr(data, filename)
        elif choice == '2':
            filename = input("Enter the filename of the QR code image to decode (e.g., 'qrcode.png'): ")
            decode_qr(filename)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    QrCode()
