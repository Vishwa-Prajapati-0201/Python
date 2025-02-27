# Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class Password_Manager:
    

    def __init__(self, initial_password):
        self.old_passwords = [initial_password]
    

    def get_password(self):
        return self.old_passwords[-1]
    
    

    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        

        else:
            print("this password already matches the previous passwords.")
    
    def is_correct(self,string):
        return string == self.get_password()
    
c1 = Password_Manager(input("Enter password you initially want : "))
print("your current password is : ")
print(c1.get_password())

c1.set_password(input("enter the new password that you want to set : "))
print(f"now your new password is set as : {c1.get_password()}")

print('''
      
    you should verfiy your new password ,
    for the that enter the new password again 
    if it returns True then it is verified and if it returns 
    False then you entered wrong password : ''')

print(c1.is_correct(input()))