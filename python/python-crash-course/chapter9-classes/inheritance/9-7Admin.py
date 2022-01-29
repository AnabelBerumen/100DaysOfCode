class Users:
    
    def __init__(self,first_name,last_name,ocupation,age):
        self.first_name = first_name
        self.last_name = last_name
        self.ocupation = ocupation
        self.age = age
        self.login_attempts = 1

    def describe_user(self):
        print(f"Name: {self.first_name}\nLast name: {self.last_name}\nOcupation: {self.ocupation}\nAge: {self.age}")
        

    def greet_user(self):
        print (f"Hello {self.first_name} {self.last_name} have a good day")


    def increment_logig_attempts(self):

        self.login_attempts = self.login_attempts +1

  
    def reset_login_attempts(self):

        self.login_attempts = 0


class Admin(Users):
    def __init__(self, first_name, last_name, ocupation, age):
        super().__init__(first_name, last_name, ocupation, age)
        self.privileges = []
    
    def show_privileges(self):
        print("List of privileges")
        for privilege in self.privileges:
           
            print(f"-{privilege.title()}")


userA = Users("Lauren","Jauregui","Singer",25)
userB = Admin("Ada", "Lovelace", "programmer", 36)

userB.privileges = ["can add post", "can delete post", "can ban user"]

userB.show_privileges()
userB.describe_user()