"""
# Student Name: Asmita Shrestha (CDU Danala)
# Student Id: 398027
# Assignment: 1 
# Group: DAN/EXT 14

#Write a program that asks the user to input a password and check its strength
#Weak: Less than 6 characters
#Medium:6-10 characters and contains at least one digit
#Strong: More than 10 characters and contains at least one digit and at least one uppercase letter
"""
inputPassword = input("Enter a password:") #ask the user to input a password

#function that is declare to check the strength of the password
def check_password_strength(password):
  length=len(password) #variable define to check the length of the password
  check_digit= any(ch.isdigit() for ch in password) #check_digit is a variable that is defined to check a  digit in a password,
  check_uppercaseletter =any(ch.isupper() for ch in password)                                                #isdigit() is a python built in function that is used to check wheather it is digit or not
                                                    #for loop is used to iterate the password and check wheather there is a digit present in a password or not
  if length < 6:  #if length of the password is less than 6 then this condtion will run and return the message password is weak
    return "Password is Weak"
  elif 6<=length<=10:   # if length of the password is more than or equal to 6 but not more than 10 then this will run
    if check_digit: #if above condition verifies and password contain at least one digit then this condition is true
       return "Password is Medium"
    else:  #if password contain 6 or more than 6 characters but doesn't contain digit then this condition will be true
      return "Password is Weak"
  else:  
    if length>10 and check_digit and check_uppercaseletter: #if length of the password is greater than 10 and contain both digit and uppercase letter then this condition will becme true
      return "Password is Strong"
    else:      # if above condtion became false then this will run 
      return "Password is Weak"
    
strength_of_password = check_password_strength(inputPassword) #call the function check_password_strength(inputpassword) to place the password and check the strength of the password
print("password strength:", strength_of_password) #this line will print the password strength i.e; weak,medium and strong
