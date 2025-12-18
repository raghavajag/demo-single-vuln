import os
import sqlite3
import subprocess

# ❌ Hardcoded secret
DB_PASSWORD = "password123"

def get_user(user_id):
    # ❌ SQL Injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    return cursor.fetchall()


def execute_command(user_input):
    # ❌ Command Injection
    os.system("echo " + user_input)


def execute_command_subprocess(user_input):
    # ❌ Command Injection (subprocess with shell=True)
    subprocess.call(user_input, shell=True)


def read_any_file(path):
    # ❌ Path Traversal
    with open(path, "r") as f:
        return f.read()


def calculate(expression):
    # ❌ Code Injection
    return eval(expression)


def insecure_login(password):
    # ❌ Insecure comparison & hardcoded credentials
    if password == DB_PASSWORD:
        return True
    return False


# ❌ Insecure temporary file handling
def write_temp(data):
    temp_file = "/tmp/app_temp.txt"
    with open(temp_file, "w") as f:
        f.write(data)


if __name__ == "__main__":
    print(get_user("1 OR 1=1"))
    execute_command("hello && rm -rf /")
    execute_command_subprocess("ls -la")
    print(read_any_file("../../etc/passwd"))
    print(calculate("__import__('os').system('whoami')"))
