passwords = [str(i) for i in input("Enter passwords:\n").split(",")]
spl_char = ["$", "#", "@"] #ABd1234@1

correctpass = []
for password in passwords:
    if (len(password) < 6 or len(password) > 12):
        continue
    if (password.isupper() or password.islower()):
        continue
    spl = any(letter in spl_char for letter in password) #spl=['#']
    if (not spl):
        continue
    num=any(letter.isdigit() for letter in password) #num=(1,2,3,4,1)
    if (not num):
        continue

    correctpass.append(password)
print()
print("Correct password is: ")