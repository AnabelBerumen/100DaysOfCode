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
userA = Users("Lauren","Jauregui","Singer",25)

userA.describe_user()
userA.greet_user()

userA.increment_logig_attempts()
print(userA.login_attempts)
userA.increment_logig_attempts()
print(userA.login_attempts)
userA.reset_login_attempts()
print(userA.login_attempts)

