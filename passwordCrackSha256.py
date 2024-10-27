import hashlib

def convertedSha256(text):
    digest = hashlib.sha256(text.encode()).hexdigest()
    return digest

userSha256 = input("Enter Your SHA256 encrypted password: ")
cleanedUserSha = userSha256.strip().lower()

found = False

with open("pass.txt", "r") as f:
    for line in f:
        password = line.strip()
        convertedUserSha256 = convertedSha256(password)
        if cleanedUserSha == convertedUserSha256:
            print(f"Password found: {password}")
            found = True
            break

if not found:
    print("Sorry, the password is not in the source file!")
