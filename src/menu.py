from face_recognize import face_recognize
from train import train_faces
import mysql_python
from keypad_basic_code import key_pressed

if __name__ == '__main__':
    choice = -1
    while choice != 3:
        print("\n___Welcome to Package Anti-Theft System  !!___\n")
        print("1) Incoming Package")
        print("2) Take Package")
        print("3) Exit System")

        print("Your choice : ")
        choice = key_pressed()
    
        if choice == 1:
            pass
        
        elif choice == 2:
            student = face_recognize()
            # Insert barcode scanning function here
            print(student)
        
        elif choice == 3:
            break

        elif choice == 4:
            mysql_python.display_data()
        else:
            print("Invalid Choice. Please Try Again...")
        
            
