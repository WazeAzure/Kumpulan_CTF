from PIL import Image

def decode_lsb(image_path):
    
    # Open the image
    img = Image.open(image_path)

    # Get the width and height of the image
    width, height = img.size

    # Initialize variables to store the hidden message and a counter for the bit position
    hidden_message = ""
    bit_position = 0

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            # Iterate through the RGB channels (Red, Green, Blue)
            for color_channel in range(3):
                # Get the least significant bit (LSB) of the color channel
                lsb = pixel[color_channel] & 1

                # Append the LSB to the hidden_message
                hidden_message += str(lsb)

                # Increment the bit position
                bit_position += 1

                # Check if we have reached the end of the message (8 bits)
                if bit_position % 8 == 0:
                    # Convert the 8-bit binary string to a character and add it to the result
                    hidden_char = chr(int(hidden_message, 2))
                    # Check if the character is the end of message marker
                    if hidden_char == '11111111':
                        return hidden_message[:-8]  # Remove the end of message marker and return the result
                    hidden_message = ""  # Reset the hidden message buffer

    return "No hidden message found"

if __name__ == "__main__":
    image_path = "paus.png"  # Replace with the path to your image
    decoded_message = decode_lsb(image_path)
    print("Decoded Message:")
    print(decoded_message)
