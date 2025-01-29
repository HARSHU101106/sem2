import re
def track_login_attempts():
    for i in range(5):
        username = input("Enter username: ")
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'
        if re.match(pattern, username):
            print("Login Succeeded")
            break
        else:
            print(f"Login Failed,{5-i-1} attempts more")
    else:
        print("oops!no more attempts")
track_login_attempts()

    