import json
import string
import random 
from pathlib import Path
from datetime import datetime

class Library:
    database='library.json'
    data={"book":[],"member":[]}
    if Path(database).exists():
        with open(database,"r") as f:
            content=f.read().strip()
            if content:
                data=json.loads(content)
    else:
        with open(database,"w") as f:
            json.dump(data,f,indent=4)
    @classmethod        
    def save_data(cls):
        with open(cls.database,"w") as f:
            json.dump(cls.data, f, indent=4,default=str)



    def gen_id(Prefix="B"):
        random_id="" 
        for i in range(5):
            random_id+=random.choice(string.ascii_uppercase + string.digits)
        return Prefix+"-"+random_id


    def add_books(self):
        title=input("enter book title: ")
        author=input("enter author name: ")
        copies=int(input("enter no of copies: "))

        books = {
            "id": Library.gen_id(),
            "title": title,
            "author": author,
            "copies": copies,
            "avaivale_copies":copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        Library.data['book'].append(books)
        Library.save_data()
    def list_books(self):
        if not Library.data["book"]:
            print("sorry no books found")
            return# return means function will stop here 
        for b in Library.data["book"]:
            print(f"{b['id']:12}{b['title'][:24]:25}{b["author"][:19]:20}{b['copies']}/{b["avaivale_copies"]:>3}")
        print()
hello=Library()

print("="*50)
print("Library Management system")
print("="*50)
print("1. Add Book")
print("2. List Book")
print("3. Add Member")
print("4. List member")
print("5. Borrow Book")
print("6. Return Book")
print("0. Exit the portal")
print("-"*50)
choice=input("What task you want to do?")
if choice=="1":
    hello.add_books()
if choice=="2":
    hello.list_books()
