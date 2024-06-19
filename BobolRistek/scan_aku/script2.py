import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Function to read a QR code from an image
def read_qr_code(image_path):
    # Open the image
    img = Image.open(image_path)

    # Decode the QR code
    decoded_objects = decode(img)

    if decoded_objects:
        # Extract and return the QR code data
        qr_code_data = decoded_objects[0].data.decode('utf-8')
        return qr_code_data
    else:
        return None

# Example usage
if __name__ == "__main__":
    l = ""
    for i in range(1, 724):

        image_path = f"{i}.png"  # Replace with the path to your image
        qr_code_data = read_qr_code(image_path)[2:]
        l += qr_code_data
    
    f = open("s_result.png", "wb")
    f.write(bytes.fromhex(l))
    print(l)

