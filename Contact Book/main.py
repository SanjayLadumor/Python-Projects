from contactbook import ContactBook

def main():
    running = True
    con = ContactBook()
    con.load_contacts()
    while running:
        print("""===== CONTACT BOOK =====

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Save Contacts
7. Load Contacts
8. Exit""")
        
        try:
            a = int(input("Enter Your Selection: "))
            if a==1:
                con.add_contact()
            elif a==2:
                con.view_contacts()
            elif a==3:
                con.search_contact()
            elif a==4:
                con.update_contact()
            elif a==5:
                con.delete_contact()
            elif a==6:
                con.save_contacts()
            elif a==7:
                con.load_contacts()
            elif a==8:
                running = False
            else:
                print("Please Select From Given Options.")
        except ValueError:
            print("Please Enter Integer")
            running = True

main()