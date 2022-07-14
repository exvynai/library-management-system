class User:
    def acquire_data(self):
        user_name = input("Enter Username: ")
        user_id = input("Enter User ID: ")
        school_name = input("Enter School name: ")
        address = input("Enter address: ")
        phone_no = input("Enter Phone number: ")
        email_id = input("Enter Email ID: ")
        dob = input("Enter Date of Birth: ")
        age = input("Enter Age: ")

        return f"{user_name};{user_id};{school_name};{address};{phone_no};{email_id};{dob};{age}\n"

    def search_user(self, username, userid):
        file = open('data/users.txt', 'r')
        for line in file:
            userdata = line.split(";")
            if userdata[0] == username and userdata[1] == userid:
                return f"Username: {userdata[0]}\nUser ID: {userdata[1]}\nSchool: {userdata[2]}\nAddress: {userdata[3]}\nPhone no: {userdata[4]}\nEmail ID: {userdata[5]}\nDOB: {userdata[6]}\nAge: {userdata[7]}\n"

        return "User doesn't exist!"

    def add_user(self):
        userdata = self.acquire_data()

        if self.search_user(userdata[0], userdata[1]) == "User doesn't exist!":
            file = open('data/users.txt', 'a+')
            file.write(userdata)
            file.close()
        else:
            print("User already exists!")
  

        print("USER ADDED SUCCESSFULLY!")

    def delete_user(self, username, userid):
        # deletes the line
        with open("data/users.txt", 'r+') as fp:
            lines = fp.readlines()
            user_loc = int()
            for line in lines:
                data = line.split(";")
                if data[0] == username and data[1] ==  userid:
                    user_loc = lines.index(line)
            fp.seek(0)
            # truncate the file
            fp.truncate()
            for number, line in enumerate(lines):
                if number not in [user_loc]:
                    fp.write(line)

        print("USER DELETED SUCCESSFULLY!")


    def edit_user(self, username, userid):
        userdata = self.search_user(username, userid)
        if userdata == "User doesn't exist!":
            return f"{username} doesn't exist"
        else:
            print("USER DETAILS:")
            print(userdata)

            choice = input("Would you like to edit? (y/n): ")
            if choice.lower() == 'y':
                #first delete user and then add new user
                self.delete_user(username, userid)
                self.add_user()
            else:
                return "No changes have occurred!"
        
        print("UPDATED USER DETAILS!")
        
def main():
    u = User()
    u.edit_user("viraj", "042")
    
if __name__ == '__main__':
    main()
