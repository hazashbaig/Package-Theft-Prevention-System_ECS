from face_recognize import face_recognize
import mysql_python
import barcode_scanner
import time


if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print("\n___Welcome to Package Anti-Theft System  !!___\n")
        print("1) Incoming Package (for delivery personnel)")
        print("2) Enter into package room to collect package")
        print("3) Exit out of package room after collecting package")
        print("4) Give Feedback")

        print("Your choice : ")
        choice = int(input())
    
        if choice == 1:
            person = face_recognize()
            print(person)

            if person == "unknown":
                print("Keep the package inside")
                print("servo opened")
                time.sleep(6)
                print("servo closed")
            else:
                print("You are student")

        elif choice == 2:
            student = face_recognize()
            print(student)

            orders = mysql_python.student_orders(student)

            if orders:
                print(f"You have {len(orders)} package(s) to collect")
                print("servo opened")
                time.sleep(6)
                print("servo closed")
            else:
                print("You have no orders to take pls go away")

        elif choice == 3:
            student = face_recognize()
            print(student)

            order_no = barcode_scanner.get_barcode()
            print(order_no)

            mysql_python.delete_order_for_student(student, order_no)

            print("servo opened")
            time.sleep(6)
            print("servo closed")

        elif choice == 4:
            student = face_recognize()
            print(f"{student} you may write the review please: ")
            review = mysql_python.enterText()
            mysql_python.storeReview(student, review)
            print(f"Thanks for the feedback {student}")

        elif choice == 0:
            break
        else:
            print("Invalid Choice. Please Try Again...")
        
            
