class Book:
    def acquire_data(self):
        title = input("Enter the Title of the book: ")
        author = input("Enter the name of the Author: ")
        publisher = input("Enter the name of the Publisher: ")
        year = input("Enter the year of publishing: ")
        price = input("Enter the price of the book")
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

def main():
    b = Book()
    # b.add_book()
    # print(b.search_book("My book", "viraj"))
    # b.delete_book("My book", "viraj")


if __name__ == '__main__':
    main()

