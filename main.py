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
    def add_members(self):
        name=input("enter  name: ")
        email=input("enter  email: ")
        borrowed=[]

        members = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed":[],
          
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        Library.data['member'].append(members)
        Library.save_data()
    def list_members(self):
        if not Library.data["member"]:
            print("sorry no member found")
            return# return means function will stop here 
        for m in Library.data["member"]:
            print(f"{m['id']:12}{m['name'][:24]:25}{m["email"][:19]:20}:>3")
        print(f"This guy has currently{m["borrowed"]}")
        print()
    def borrow_book(self):
        member_id = input("enter the member id")
        memberss = [m for m in Library.data['member'] if m['id'] == member_id]
        if not memberss:
            print("sorry no such member found")
            return
        member=memberss[0]
    
        book_id = input("enter the book id")
        bookss = [b for b in Library.data['book'] if b['id'] == book_id]
        if not bookss:
            print("sorry no such book found")
            return
        book=bookss[0]
        if  book['avaivale_copies']<=0:
            print("sorry no books available")
            return
        borrow_entry={
            "title":book['title'],
             "id":book['id'],
             "borrowed-on":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

        }
        member['borrowed'].append(borrow_entry)
        book['avaivale_copies']-=1
        Library.save_data()
    def return_book(self):
            member_id = input("enter the member id")
            memberss = [m for m in Library.data['member'] if m['id'] == member_id]
            if not memberss:
                print("sorry no such member found")
                return
            member=memberss[0]
            if not member['borrowed']:
                print("No borrowed books")
                return
            print("Borrowed books")
            for i,b in enumerate(member['borrowed'],start=1):
                print(f"{i}.{b['title']}({b['id']})")
            try:
                choice=int(input("enter no to return - "))
                select=member['borrowed'].pop(choice-1)
            except Exception as err:
                print("invalid value")  
            books=[bk for bk in Library.data['book'] if bk['id']==select['id']] 
            if books:
                books[0]['avaivale_copies']+=1
            Library.save_data()

        
           


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
if choice=="3":
    hello.add_members()
if choice=="4":
    hello.list_members()
if choice=="5":
    hello.borrow_book()
if choice=="6":
    hello.return_book()
if choice=="0":
    exit(0)
