# to print the user name of a given email address.
# email addresses in the "username@companyname.com" format
# Hints:
#

emailAddress = input("Enter your email address: ")
userName = emailAddress.split("@")
print(userName[0])
