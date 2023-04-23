import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

def compress_image():
    # Prompt user to select image file
    filename = filedialog.askopenfilename(title="Select an image file to compress")

    # Check if user canceled file selection
    if not filename:
        return

    try:
        # Load image
        img = cv2.imread(filename)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Huffman coding
        huffmanen = cv2.imencode('.png', gray, [cv2.IMWRITE_PNG_COMPRESSION, 9])[1]

        # Save compressed image
        with open('compressed.png', 'wb') as f:
            f.write(huffmanen)

        # Display original and compressed images
        cv2.imshow('Original Image', img)
        cv2.imshow('Compressed Image', cv2.imread('compressed.png'))

    except Exception as e:
        # Display error message if image processing fails
        error_msg = f"Error: {e}"
        error_label.config(text=error_msg)

    finally:
        # Enable compress button and clear error message
        compress_button.config(state=NORMAL)
        error_label.config(text='')

def decompress_image():
    # Prompt user to select compressed image file
    filename = filedialog.askopenfilename(title="Select a compressed image file to decompress")

    # Check if user canceled file selection
    if not filename:
        return

    try:
        # Load compressed image
        with open(filename, 'rb') as f:
            img_data = f.read()

        # Apply Huffman coding
        img_array = np.frombuffer(img_data, dtype=np.uint8)
        huffmande = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Save decompressed image
        cv2.imwrite('decompressed.png', huffmande)

        # Display decompressed image
        cv2.imshow('Decompressed Image', huffmande)

    except Exception as e:
        # Display error message if image processing fails
        error_msg = f"Error: {e}"
        error_label.config(text=error_msg)

    finally:
        # Enable decompress button and clear error message
        decompress_button.config(state=NORMAL)
        error_label.config(text='')

# Create GUI
root = Tk()
root.title("Medical Image Compression")
root.geometry("400x200")

compress_button = Button(root, text="Compress Image", command=compress_image)
compress_button.pack()

decompress_button = Button(root, text="Decompress Image", command=decompress_image)
decompress_button.pack()

error_label = Label(root, text='')
error_label.pack()

root.mainloop()
