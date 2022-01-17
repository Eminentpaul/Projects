email = input("What is your email address?: ")

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

result = f"Your username is '{username}' and your Domain is '{domain}'"

print(result)
# print(email.index(0))