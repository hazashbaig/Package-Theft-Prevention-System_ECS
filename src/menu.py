from face_recognize import face_recognize
from train import train_faces

if __name__ == '__main__':
    choice = -1
    while choice != 3:
        print("\n___Welcome to Package Anti-Theft System  !!___\n")
        print("Do you want to :")
        print("1) Train Faces")
        print("2) Take Delivery")
        print("3) Exit System")

        print("Your choice : ")
        choice = int(input())
        
        if choice == 1:
            train_faces()
        
        elif choice == 2:
            student = face_recognize()
            # Insert barcode scanning function here
            print(student)
        
        elif choice == 3:
            break
        else:
            print("Invalid Choice. Please Try Again...")
        
            
