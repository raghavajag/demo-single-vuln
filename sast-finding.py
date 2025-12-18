import os
import sqlite3

def get_user(username):
    # ❌ SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


def run_command(cmd):
    # ❌ Command Injection vulnerability
    os.system(cmd)


def read_file(filename):
    # ❌ Path Traversal vulnerability
    with open(filename, "r") as f:
        return f.read()


def login(user_input_password):
    # ❌ Hardcoded secret
    admin_password = "Admin@123"

    if user_input_password == admin_password:
        return True
    return False


# ❌ Insecure use of eval
def calculate(expression):
    return eval(expression)


# Example usage
if __name__ == "__main__":
    print(get_user("admin' OR '1'='1"))
    run_command("ls -la")
    print(read_file("../../etc/passwd"))
    print(calculate("2 + 3"))
