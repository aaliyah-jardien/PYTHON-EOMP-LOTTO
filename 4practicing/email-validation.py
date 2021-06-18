# # PYTHON PROGRAM TO VALIDATE AN EMAIL ADDRESS
# # RE MODULE PROVIDES SUPPORT
# # FOR REGULAR EXPRESSIONS
import re
# # MAKE A REGULAR EXPRESSION FOR VALIDATING AN EMAIL
# regex = "b[A-Z0-9._%+-]+@[A-Z0-9.-]+\[A-Z]{2,}\b"
#
#
# # FUNCTION
# def check(mail):
#     # PASS THE REGULAR EXPRESSION & THE STRING IN SEARCH() METHOD
#     if re.search(regex, mail):
#         print("Valid Email")
#     else:
#         print("Invalid Email")
#
#
# # # DRIVER CODE
# # if __name__ == "__main__":
# #     # ENTER THE EMAIL
# #     email = input("Enter Email Address: ")
# #     #email = "aaliyahjar13@gmail.com"
# #     # CALLING RUN FUNCTION
# #     check(email)
#
# def check2():
#     regex = "b[A-Z0-9._%+-]+@[A-Z0-9.-]+\[A-Z]{2,}\b"
#
#     email = input("user: ")
#     for i in range(len(email)):
#         if re.search(regex, email):
#             print("Valid")
#         else:
#             print("Invalid")
#
#
# check2()

def email_info():
    ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    mail32 = input('user email: ')

    for i in range(len(mail32)):
        if re.search(ex, mail32):
            with open("text_file.txt", "w+") as f:
                f.write(mail32)
                f.write('\n')

        else:
            f.write('invalid')

email_info()

# well done , you did it
