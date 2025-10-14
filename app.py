"""
Demo Single Vulnerability Test Case
===================================

This file contains a single SQL injection sink with 4 different attack paths,
each consisting of 4-6 function calls in the chain.

SINK: execute_query() - executes SQL queries

ATTACK PATHS:
1. Path 1 (4 functions): web_handler -> process_data -> validate_input -> execute_query
2. Path 2 (5 functions): api_handler -> process_request -> validate_params -> sanitize_data -> execute_query
3. Path 3 (6 functions): admin_handler -> process_admin -> validate_admin -> transform_data -> check_permissions -> execute_query
4. Path 4 (5 functions): user_handler -> process_user -> validate_user -> authenticate -> execute_query
"""

import sqlite3
import logging
from typing import Dict, List, Optional

# Database connection
def get_db_connection():
    """Get database connection"""
    return sqlite3.connect(':memory:')

# =====================================
# SINK FUNCTION - SQL Injection Vulnerability
# =====================================

def execute_query(query: str, params: Optional[List] = None) -> List[Dict]:
    """
    SINK: Executes SQL query directly without proper sanitization
    This is vulnerable to SQL injection
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # VULNERABILITY: Direct execution without proper escaping
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)  # This is the vulnerable line

        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        return [dict(zip(columns, row)) for row in results]
    finally:
        conn.close()

# =====================================
# ATTACK PATH 1: 4 Functions
# =====================================

def web_handler(request_data: Dict) -> Dict:
    """Entry point 1: Web request handler"""
    user_input = request_data.get('query', '')
    return process_data(user_input)

def process_data(input_data: str) -> Dict:
    """Process user data"""
    processed = f"SELECT * FROM users WHERE name = '{input_data}'"
    return validate_input(processed)

def validate_input(query_string: str) -> Dict:
    """Basic validation (insufficient)"""
    if len(query_string) > 10:  # Basic check
        return execute_query(query_string)
    return {"error": "Query too short"}

# =====================================
# ATTACK PATH 2: 5 Functions
# =====================================

def api_handler(request: Dict) -> Dict:
    """Entry point 2: API request handler"""
    params = request.get('params', [])
    return process_request(params)

def process_request(parameters: List) -> Dict:
    """Process API request parameters"""
    param_str = str(parameters[0]) if parameters else ""
    return validate_params(param_str)

def validate_params(param: str) -> Dict:
    """Parameter validation"""
    if param and len(param) > 3:
        return sanitize_data(param)
    return {"error": "Invalid parameter"}

def sanitize_data(dirty_data: str) -> Dict:
    """Attempted sanitization (insufficient)"""
    # This sanitization is incomplete and can be bypassed
    clean = dirty_data.replace("'", "''")  # Only handles single quotes
    query = f"SELECT * FROM products WHERE id = '{clean}'"
    return execute_query(query)

# =====================================
# ATTACK PATH 3: 6 Functions
# =====================================

def admin_handler(admin_request: Dict) -> Dict:
    """Entry point 3: Admin panel handler"""
    admin_data = admin_request.get('admin_query', '')
    return process_admin(admin_data)

def process_admin(admin_input: str) -> Dict:
    """Process admin input"""
    return validate_admin(admin_input)

def validate_admin(input_str: str) -> Dict:
    """Admin input validation"""
    if input_str.startswith('ADMIN:'):
        return transform_data(input_str[6:])  # Remove ADMIN: prefix
    return {"error": "Not admin request"}

def transform_data(data: str) -> Dict:
    """Transform admin data"""
    transformed = data.upper()
    return check_permissions(transformed)

def check_permissions(perm_data: str) -> Dict:
    """Check permissions (bypassed)"""
    # This check can be bypassed
    if len(perm_data) > 5:
        query = f"SELECT * FROM admin_logs WHERE action = '{perm_data}'"
        return execute_query(query)
    return {"error": "Permission denied"}

# =====================================
# ATTACK PATH 4: 5 Functions
# =====================================

def user_handler(user_request: Dict) -> Dict:
    """Entry point 4: User profile handler"""
    user_id = user_request.get('user_id', '')
    return process_user(user_id)

def process_user(user_identifier: str) -> Dict:
    """Process user identifier"""
    return validate_user(user_identifier)

def validate_user(user_id: str) -> Dict:
    """User ID validation"""
    if user_id.isdigit():
        return authenticate(user_id)
    return {"error": "Invalid user ID"}

def authenticate(user_id: str) -> Dict:
    """Authentication check (insufficient)"""
    # This authentication can be bypassed
    query = f"SELECT * FROM users WHERE id = {user_id} AND active = 1"
    return execute_query(query)

# =====================================
# Additional Helper Functions
# =====================================

def setup_database():
    """Setup test database"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create test tables
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        active INTEGER DEFAULT 1
    )''')

    cursor.execute('''CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )''')

    cursor.execute('''CREATE TABLE admin_logs (
        id INTEGER PRIMARY KEY,
        action TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    # Insert test data
    cursor.execute("INSERT INTO users (name, active) VALUES ('admin', 1)")
    cursor.execute("INSERT INTO users (name, active) VALUES ('user', 1)")
    cursor.execute("INSERT INTO products (name, price) VALUES ('test', 10.99)")
    cursor.execute("INSERT INTO admin_logs (action) VALUES ('login')")

    conn.commit()
    conn.close()

# =====================================
# Main Application Entry Points
# =====================================

def main():
    """Main application"""
    setup_database()
    print("Demo Single Vulnerability Application Started")
    print("Available endpoints:")
    print("1. web_handler(request_data)")
    print("2. api_handler(request)")
    print("3. admin_handler(admin_request)")
    print("4. user_handler(user_request)")
    print("\nAll paths lead to vulnerable execute_query() function")

if __name__ == "__main__":
    main()
