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
                return f"Title: {bookinfo[0]}\nAuthor: {bookinfo[1]}\nPublisher: {bookinfo[3]}\nYear: {bookinfo[4]}\nPrice: {bookinfo[5]}\nSchool Name: {bookinfo[6]}\n"

        return "Book doesn't exist!"

    def add_book(self):
        bookinfo = self.acquire_data()

        if self.search_book(bookinfo[0], bookinfo[1]) == "Book doesn't exist!":
            file = open('data/books.txt', 'a+')
            file.write(bookinfo)
            file.close()
        else:
            print("Book already exists!")

    

def main():
    b = Book()
    b.add_book()

if __name__ == '__main__':
    main()

