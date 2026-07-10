library = [{
    "id":11,
    "title":"Atomic Habits",
    "author":"James Clear",
    "available":True,
}]

def find_id(a):
    for i in range(len(library)):
        if a==library[i]["id"]:
            return library[i]
    else:
        return False

def add_book():
    new = {}
    a = int(input("Enter ID: "))
    data = find_id(a)
    if data==False:
        new["id"] = a
        new["title"] = input("Book Title: ")
        new["author"] = input("Author: ")
        new["available"] = True
        library.append(new)
        return library
    else:
        print("ID Already Exists")

def display_all_books():
    for book in library:
        print(f"""
-------------------------
ID        : {book["id"]}
Title     : {book["title"]}
Author    : {book["author"]}
Available : {book["available"]}
-------------------------
""")

def search_books():
    a = int(input("Enter Book ID: "))
    data = find_id(a)
    if data==False:
        return f"Book Not Available"
    else:
        if data["available"]:
            return "Book is available"
        else:
            return "Book is currently borrowed"

def borrow_book():
    a = int(input("Enter Book ID to Borrow: "))
    for i in range(len(library)):
        if a==library[i]["id"]:
            if library[i]["available"]==True:
                library[i]["available"]=False
                return f"You Borrowed This Book"
            else:
                return f"Book Already Borrowed"
    else:
        return f"Book Not Available"
    
def return_book():
    a = int(input("Enter Book ID to Return: "))
    for i in range(len(library)):
        if a==library[i]["id"]:
            if library[i]["available"]==False:
                library[i]["available"]=True
                return f"Book Returned"
            else:
                return f"Book Already Returned"
    else:
        return f"Book Not Available"
    
def delete_book():
    a = int(input("Enter Book ID to Delete: "))
    data = find_id(a)
    if data==False:
        return f"Book Does Not Exist"
    else:
        library.remove(data)
        return "Book Deleted Successdully"

def main():
    Ongo = True
    while Ongo!=False:
        print("Select Action: ")
        print("""
            1. Add Book
            2. Display All Books
            3. Search Book
            4. Borrow Book
            5. Return Book
            6. Delete Book
            7. Exit
            """)
        
        a = int(input("Your Selection: "))
        if a==1:
            print(add_book())
            Ongo = True
        elif a==2:
            display_all_books()
            Ongo = True
        elif a==3:
            print(search_books())
            Ongo = True
        elif a==4:
            print(borrow_book())
            Ongo = True
        elif a==5:
            print(return_book())
            Ongo = True
        elif a==6:
            print(delete_book())
            Ongo = True
        elif a==7:
            Ongo = False
        else:
            print("Please Select From Available Options")
            Ongo = True

main()