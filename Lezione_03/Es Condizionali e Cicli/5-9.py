username:list = ["Gigi", "Tony", "admin", "Pier", "Lulu"]
for p in range(len(username)):
    if username[p] == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username[p]}, thank you for logging in again")

username = []
if username == []:
    print("We need to find some users")