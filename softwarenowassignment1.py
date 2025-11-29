#Write a program that asks the user to input a password and check its strength
#Weak: Less than 6 characters
#Medium:6-10 characters and contains at least one digit
#Strong: More than 10 characters and contains at least one digit and at least one uppecase letter

inputPassword = input("Enter a password:") #ask the user to input a password

#function that is declare to check the strength of the password
def check_password_strength(password):
  length=len(password) #variable define to check the length of the password
  check_digit= any(ch.isdigit() for ch in password) #check_digit is a variable that is defined to check a  digit in a password,
                                                    #isdigit() is a python built in function that is used to check wheather it is digit or not
                                                    #for loop is used to iterate the password and check wheather there is a digit present in a password or not
  if length < 6:
    return "Password is weak"
  elif 6<=length<=10:
    if check_digit:
       return "Password is medium"
    else:
      return "Password is weak"
  else:
    return "Password is weak"
strength_of_password = check_password_strength(inputPassword)
print("password strength:", strength_of_password)