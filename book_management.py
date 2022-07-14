class Book:
    def acquire_data(self):
        title = input("Enter the Title of the book: ")
        author = input("Enter the name of the Author: ")
        publisher = input("Enter the name of the Publisher: ")
        year = input("Enter the year of publishing: ")
        price = input("Enter the price of the book: ")
        school_name = input("Enter the name of the school: ")

        return f"{title};{author};{publisher};{year};{price};{school_name}\n"

    def search_book(self, bookname, author):
        file = open('data/books.txt', 'r')
        for line in file:
            bookinfo = line.split(";")
            if bookinfo[0] == bookname and bookinfo[1] == author:
                return f"Title: {bookinfo[0]}\nAuthor: {bookinfo[1]}\nPublisher: {bookinfo[2]}\nYear: {bookinfo[3]}\nPrice: {bookinfo[4]}\nSchool Name: {bookinfo[5]}\n"

        return "Book doesn't exist!"

    def add_book(self):
        bookinfo = self.acquire_data()

        if self.search_book(bookinfo[0], bookinfo[1]) == "Book doesn't exist!":
            file = open('data/books.txt', 'a+')
            file.write(bookinfo)
            file.close()

            print("Book added Successfully!")
        else:
            print("Book already exists!")

    def delete_book(self, bookname, author):
        if self.search_book(bookname, author) == "Book doesn't exist!":
            print("The book doesn't exist!")
        else:
            with open("data/books.txt", 'r+') as fp:
                lines = fp.readlines()
                book_loc = int()
                for line in lines:
                    data = line.split(";")
                    if data[0] == bookname and data[1] == author:
                        book_loc = lines.index(line)
                fp.seek(0)
                # truncate the file
                fp.truncate()
                for number, line in enumerate(lines):
                    if number not in [book_loc]:
                        fp.write(line)

        print("BOOK DELETED SUCCESSFULLY!")

    def edit_book(self, bookname, author):
        if self.search_book(bookname, author) == "Book doesn't exist!":
            print("The book doesn't exist!")
        else:
            file = open("data/books.txt", "r+")
            for line in file:
                data = line.split(";")
                if data[0] == bookname and data[1] == author:
                    while True:
                        choice = input("Which attribute would you like to edit?\n1 - Title\n2 - Publisher\n3 - Year\n4 - Price\n5 - School name\n6 - Quit\nEnter your choice: ")
                        if choice == '1' or choice.lower() == 'title':
                            data[0] = input("Enter new book name: ")
                            print(f"Successfully changed title to {data[0]}")
                        elif choice == '2' or choice.lower() == 'publisher':
                            data[1] = input("Enter new publisher: ")
                            print(f"Successfully changed publisher to {data[1]}")
                        elif choice == '3' or choice.lower() == 'year':
                            data[2] = input("Enter new year: ")
                            print(f"Successfully changed year to {data[2]}")
                        elif choice == '4' or choice.lower() == 'price':
                            data[3] = input("Enter new price: ")
                            print(f"Successfully changed price to {data[3]}")
                        elif choice == '5' or choice.lower() == 'school name':
                            data[4] = input("Enter new school name: ")
                            print(f"Successfully changed school name to {data[4]}")
                        elif choice == '6' or choice.lower() == 'quit':
                            break
                        else:
                            print("Invalid choice!")
        
def main():
    b = Book()
    # b.add_book()
    # print(b.search_book("My book", "viraj"))
    # b.delete_book("My book", "viraj")
    b.edit_book("my book", "viraj")

if __name__ == '__main__':
    main()

