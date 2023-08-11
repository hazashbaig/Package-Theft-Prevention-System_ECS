import cv2
from pyzbar.pyzbar import decode

def get_barcode():
    cap = cv2.VideoCapture(1)
    flag = 0
    barcode_detected = ""

    while True:
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        barcodes = decode(gray)

        for barcode in barcodes:
            
            barcode_data = barcode.data.decode('utf-8')

            if flag == 0:
                # print(f"Detected Barcode: {barcode_data}")
                barcode_detected = barcode_data
                flag = 1
            

        cv2.imshow('Barcode Detection', frame)

        # Break the loop if the 'esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

        if flag == 1:
            cap.release()
            cv2.destroyAllWindows()
            return barcode_detected


print(get_barcode())