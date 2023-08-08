import cv2
from pyzbar.pyzbar import decode
import json


def load_all_orders():
    with open('all_orders.json') as json_file:
        all_orders_data = json.load(json_file)
        return all_orders_data.get("all_orders", [])

def save_all_orders(all_orders_list):
    all_orders_data = {"all_orders": all_orders_list}
    with open('all_orders.json', 'w') as json_file:
        json.dump(all_orders_data, json_file, indent=4)

def remove_order_from_student(student_data, barcode_number):
    for student in student_data:
        if student["Student"] == "21bce7503":
            if barcode_number in all_orders:
                if barcode_number in student["Orders"]:
                    student["Orders"].remove(barcode_number)
                    remove_order_from_all_orders(barcode_number)
                    return True
    return False

def remove_order_from_all_orders(barcode_number):
    all_orders_list = load_all_orders()
    if barcode_number in all_orders_list:
        all_orders_list.remove(barcode_number)
        save_all_orders(all_orders_list)

# Load the data from data.json
with open('data.json') as json_file:
    data = json.load(json_file)

# Load all orders from all_orders.json
all_orders = load_all_orders()

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
camera = True

while camera:
    success, frame = cap.read()

    for code in decode(frame):
        barcode_number = code.data.decode('utf-8')

        # Check if barcode_number is under the student "21bce7503" and remove it from Orders if present
        if remove_order_from_student(data, barcode_number):
            print("Barcode removed from student 21bce7503 Orders:", barcode_number)
            # Save the updated data back to data.json
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
        

    cv2.imshow('Testing-code-scan', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
