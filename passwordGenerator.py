#Password Generator
#Date started: February 24th 2022
#Date ended: February 25th 2022

#Dependency Modules
import random
import string

# Global Variables
specialCharactersList = ["!","@","#","$","%","&","*"]
numberList = ["0",'1','2','3','4','5','6','7','8','9']
passwordCharacterCount = 0
generated_password = []

#Defining bank of characters desired
passwordCharList = list(string.ascii_letters)
for i in specialCharactersList:
    passwordCharList.append(i)

for i in numberList:
    passwordCharList.append(i)


################################################################################################################################

#Prompting User for desired password length
desired_password_length = input("What is your desired password length? (Recommended length of 15): ")

#Prompting user for alias of the password
temp_alias = input("What is the password for? Example: Gmail password for johnappleseed@gmail.com: ")

#Ensures password contains special charater and number to meet password requirements
generated_password.append(specialCharactersList[random.randrange(0,7)])
generated_password.append(numberList[random.randrange(0,10)])

#Loops thru and adds random character from character bank into empty array
while (passwordCharacterCount < int(desired_password_length)):
    
    random_num = random.randint(0,len(passwordCharList)-1)
    generated_password.append(passwordCharList[random_num])
    passwordCharacterCount += 1
    
################################################################################################################################

#Output the password
print(f"{temp_alias} password: {''.join(map(str,generated_password))}")

#Opens text file and appends password to the list
with open('passwords.txt', 'a') as file_object:
    file_object.write(f"{temp_alias} password: {''.join(map(str,generated_password))} \n")
    file_object.close()


