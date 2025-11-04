# login.py
# Simple user authentication example

def get_user_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def authenticate(username, password):
    # Insecure hardcoded credentials (for demonstration only)
    users = {
        "admin": "AdminPass123",
        "user1": "Password1"
    }
    return users.get(username) == password

def main():
    username, password = get_user_credentials()
    if authenticate(username, password):
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials. Access denied.")

if __name__ == "__main__":
    main()
