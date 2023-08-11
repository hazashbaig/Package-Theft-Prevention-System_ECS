from face_recognize import face_recognize
import mysql_python
import barcode_scanner


if __name__ == '__main__':
    choice = -1
    while choice != 3:
        print("\n___Welcome to Package Anti-Theft System  !!___\n")
        print("1) Incoming Package (for delivery personnel)")
        print("2) Take Package")
        print("3) Exit System")

        print("Your choice : ")
        choice = int(input())
    
        if choice == 1:
            order_no = barcode_scanner.get_barcode()
            orders = mysql_python.get_student_orders()

            if order_no in orders:
                print("You can keep the package inside")
                # Open servo
            else:
                print("Package unrecognized")
        
        elif choice == 2:
            # student = face_recognize()
            # student_orders = mysql_python.get_student_orders(student)

            # Insert barcode scanning function here
            # print(student)
            pass
        
        elif choice == 3:
            break
        
        else:
            print("Invalid Choice. Please Try Again...")
        
            
