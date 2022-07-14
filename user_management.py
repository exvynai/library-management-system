class User:
    
    def acquire_data():
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
                # print(userdata)
                # print(userdata[0], userdata[1])
                return f"Username: {userdata[0]}\nUser ID: {userdata[1]}\nSchool: {userdata[2]}\nAddress: {userdata[3]}\nPhone no: {userdata[4]}\nEmail ID: {userdata[5]}\nDOB: {userdata[6]}\nAge: {userdata[7]}\n"

        return "User doesn't exist!"

    def add_user(self):
        userdata = self.acquire_data()

        file = open('data/users.txt', 'a+')
        if self.search_user(userdata[0], userdata[1]) == "User doesn't exist!":
            file.write(userdata)
        else:
            print("User already exists!")
        file.close()

    def edit_user(self, username, userid):
        file = open('data/users.txt', 'r')
        for line in file:
            userdata = line.split(";")
            if userdata[0] == username and userdata[1] == userid:
                #use add user function, but edited
                #need to change the add user function
                pass
            
        print("User doesn't exist!")

        

def main():
    u = User("viraj", "042", "cse", "hennur", "8919387058", "vir200319@gmail.com", "19/11/03", "18")
    # u.add_user()
    # u2 = User("testuser", "045", "ece", "hennur", "8919387058",  "vir200319@gmail.com", "19/11/03", "18")
    # u2.add_user()
    # print(u2.search_user("viraj", "042"))
    # print(u2.search_user("viraj", "04234"))
    

if __name__ == '__main__':
    main()
