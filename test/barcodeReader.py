import cv2 as cv
from pyzbar.pyzbar import decode
import os as os

def read_barcodes(image_path):
    # Load the image
    image = cv.imread(image_path)

    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Decode barcodes using pyzbar
    barcodes = decode(gray)

    if not barcodes:
        print("No barcodes found.")
        return

    # Iterate over the detected barcodes and print their data
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        print("Barcode Data:", barcode_data)
        barcode_type = barcode.type
        print("Barcode Type:", barcode_type)

        # Draw a rectangle around the barcode on the image
        (x, y, w, h) = barcode.rect
        # cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put the barcode data on the image
        # cv.putText(image, barcode_data, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with the barcodes and their data
    cv.imshow("Barcode Detection", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Example usage
image_path = os.getcwd() + "/Package-Theft-Prevention-System_ECS/test/barcode.png"  # Replace this with the path to your image file
read_barcodes(image_path)
