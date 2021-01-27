email = input("Enter ur email : ").strip()

userName = email[:email.index("@")]
domainName = email[email.index("@")+1:]
print("The email you entered is "+email+" the username is "+userName+" and the domain name is "+domainName)
