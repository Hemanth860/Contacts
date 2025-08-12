contacts=[]

def add_contact():
    print("\nEnter new contact details:")
    name=input("\nName:")
    phone=input("\nPhone:")
    email=input("\nEmail:")
    
    contact={'name':name,
             'phone':phone,
             'email':email}
    contacts.append(contact)
    print("Contact is added!!")

def view_contact():
    pass

def search_contact():
    pass

print("--- WELCOME TO YOUR CONTACT BOOK ---")

while(True):
    print("\nPlease select an option")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Quit")

    try:
        choice=int(input("Enter your choice (1-4):"))

        if choice==1:
            add_contact()

        elif choice==2:
            view_contact()

        elif choice==3:
            search_contact()

        elif choice==4:
            print("GOODBYE!!")
            break
        else:
            print("Invalid choice.Please try again.Enter a number from 1 to 4 only")

    except ValueError:
        print("Invalid input!! Please enter a number,not text.")

