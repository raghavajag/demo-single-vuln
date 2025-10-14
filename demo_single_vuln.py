"""
Demo Single Vulnerability Testing File
=====================================

Single SQL Injection Vulnerability: cursor.execute(query)
4 Attack Paths with 4-6 chained function calls each

This file demonstrates a single vulnerability with multiple attack paths
leading to the vulnerable sink: cursor.execute(query)
"""

import sqlite3
import logging
from typing import Optional, Dict, Any

class DatabaseManager:
    """Database connection and basic operations"""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None

    def connect(self) -> sqlite3.Connection:
        """Establish database connection"""
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def get_cursor(self) -> sqlite3.Cursor:
        """Get database cursor"""
        if not self.connection:
            self.connect()
        return self.connection.cursor()

class UserService:
    """User management service"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def find_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Find user by ID"""
        cursor = self.db_manager.get_cursor()
        query = f"SELECT * FROM users WHERE id = '{user_id}'"  # Vulnerable
        cursor.execute(query)  # THIS IS THE ONLY VULNERABLE SINK
        result = cursor.fetchone()
        return dict(zip(['id', 'name', 'email'], result)) if result else None

    def find_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Find user by email - SANITIZED PATH (path_3)"""
        # Input sanitization - prevent SQL injection
        import re
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return None  # Invalid email format
        return self.find_user_by_id(email)  # Call chain: 2 functions

    def find_user_by_id_safe(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Find user by ID with input validation - DEAD CODE PATH (path_1)"""
        # Input validation - prevent SQL injection
        if not user_id or not isinstance(user_id, str) or len(user_id) > 10:
            return None
        # Only allow numeric IDs
        try:
            int(user_id)
        except ValueError:
            return None
        cursor = self.db_manager.get_cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))  # Safe parameterized query
        result = cursor.fetchone()
        return dict(zip(['id', 'name', 'email'], result)) if result else None

class ContentService:
    """Content management service"""

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user_content(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get content for a user"""
        return self.user_service.find_user_by_id(user_id)  # Call chain: 3 functions

    def search_content_by_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Search content by user"""
        return self.get_user_content(user_id)  # Call chain: 4 functions

class ReportService:
    """Report generation service"""

    def __init__(self, content_service: ContentService):
        self.content_service = content_service

    def generate_user_report(self, user_id: str) -> str:
        """Generate report for user"""
        user_data = self.content_service.get_user_content(user_id)  # Call chain: 5 functions
        if user_data:
            return f"Report for user {user_data['name']}"
        return "User not found"

    def export_user_data(self, user_id: str) -> str:
        """Export user data"""
        return self.generate_user_report(user_id)  # Call chain: 6 functions

class AuthService:
    """Authentication and authorization service"""

    def __init__(self):
        self.current_user = None
        self.admin_users = ['admin', 'superuser', 'alice']  # alice is admin for demo

    def login(self, username: str, password: str) -> bool:
        """Simple login - for demo purposes"""
        if username in ['alice', 'bob'] and password == 'password':
            self.current_user = username
            return True
        return False

    def logout(self):
        """Logout current user"""
        self.current_user = None

    def is_admin(self) -> bool:
        """Check if current user is admin - PROTECTED PATH (path_2)"""
        return self.current_user in self.admin_users

    def is_authenticated(self) -> bool:
        """Check if user is authenticated - PROTECTED PATH (path_5, path_7)"""
        return self.current_user is not None

class AdminService:
    """Administrative operations"""

    def __init__(self, report_service: ReportService, auth_service: AuthService):
        self.report_service = report_service
        self.auth_service = auth_service

    def admin_user_lookup(self, user_id: str) -> str:
        """Admin user lookup - requires admin auth"""
        if not self.auth_service.is_admin():
            raise PermissionError("Admin access required")
        return self.report_service.generate_user_report(user_id)  # Call chain: 7 functions

    def admin_export_data(self, user_id: str) -> str:
        """Admin data export - requires admin auth"""
        if not self.auth_service.is_admin():
            raise PermissionError("Admin access required")
        return self.report_service.export_user_data(user_id)  # Call chain: 8 functions

class APIManager:
    """API endpoint manager"""

    def __init__(self, admin_service: AdminService, auth_service: AuthService):
        self.admin_service = admin_service
        self.auth_service = auth_service

    def api_user_profile(self, user_id: str) -> str:
        """API user profile endpoint - requires user auth"""
        if not self.auth_service.is_authenticated():
            raise PermissionError("User authentication required")
        return self.admin_service.admin_user_lookup(user_id)  # Call chain: 8 functions

    def api_admin_export(self, user_id: str) -> str:
        """API admin export endpoint - requires admin auth"""
        return self.admin_service.admin_export_data(user_id)  # Call chain: 9 functions

class WebController:
    """Web request controller"""

    def __init__(self, api_manager: APIManager, auth_service: AuthService):
        self.api_manager = api_manager
        self.auth_service = auth_service

    def handle_user_request(self, request_data: Dict[str, Any]) -> str:
        """Handle user profile request - requires user auth"""
        if not self.auth_service.is_authenticated():
            raise PermissionError("User authentication required")
        user_id = request_data.get('user_id', '')
        return self.api_manager.api_user_profile(user_id)  # Call chain: 9 functions

    def handle_admin_export(self, request_data: Dict[str, Any]) -> str:
        """Handle admin export request - requires admin auth"""
        user_id = request_data.get('user_id', '')
        return self.api_manager.api_admin_export(user_id)  # Call chain: 10 functions

class DeadCodeService:
    """Service with dead code - never called - DEAD CODE PATH (path_8)"""

    def __init__(self, content_service: ContentService):
        self.content_service = content_service

    def unused_search_method(self, user_id: str) -> Optional[Dict[str, Any]]:
        """This method is never called - dead code"""
        return self.content_service.search_content_by_user(user_id)  # This path is unreachable

# === ATTACK PATHS WITH FALSE POSITIVES ===

# === ATTACK PATH 1: Direct Vulnerable Path ===
def attack_path_1(user_input: str) -> None:
    """Attack Path 1: 4 function calls - VULNERABLE"""
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)

    # This leads to cursor.execute(query) through 4 function calls - VULNERABLE
    report_service.generate_user_report(user_input)

# === ATTACK PATH 2: Via Admin Service (PROTECTED) ===
def attack_path_2(user_input: str) -> None:
    """Attack Path 2: 6 function calls - PROTECTED (requires user auth)"""
    db = DatabaseManager()
    auth_service = AuthService()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service, auth_service)
    api_manager = APIManager(admin_service, auth_service)

    # This leads to cursor.execute(query) through 6 function calls - PROTECTED by auth
    api_manager.api_user_profile(user_input)

# === ATTACK PATH 3: Via Web Controller (PROTECTED) ===
def attack_path_3(user_input: str) -> None:
    """Attack Path 3: 7 function calls - PROTECTED (requires user auth)"""
    db = DatabaseManager()
    auth_service = AuthService()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service, auth_service)
    api_manager = APIManager(admin_service, auth_service)
    web_controller = WebController(api_manager, auth_service)

    # This leads to cursor.execute(query) through 7 function calls - PROTECTED by auth
    web_controller.handle_user_request({'user_id': user_input})

# === ATTACK PATH 4: Via Email Search (SANITIZED + PROTECTED) ===
def attack_path_4(user_input: str) -> None:
    """Attack Path 4: Multiple paths - SANITIZED (email validation) + PROTECTED (admin auth)"""
    db = DatabaseManager()
    auth_service = AuthService()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service, auth_service)
    api_manager = APIManager(admin_service, auth_service)
    web_controller = WebController(api_manager, auth_service)

    # Path 4a: Via email search (SANITIZED) - 3 function calls
    # This is SANITIZED by email validation in find_user_by_email
    result = user_service.find_user_by_email(user_input)  # SANITIZED
    if result:
        # This path would be blocked by auth checks in web_controller
        web_controller.handle_admin_export({'user_id': result['id']})  # PROTECTED

# === MAIN ENTRY POINTS ===
def main():
    """Main application entry point"""
    # Initialize the full application stack with authentication
    db = DatabaseManager()
    auth_service = AuthService()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service, auth_service)
    api_manager = APIManager(admin_service, auth_service)
    web_controller = WebController(api_manager, auth_service)

    # Initialize dead code service (never used)
    dead_code_service = DeadCodeService(content_service)

    # Setup database
    cursor = db.get_cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    cursor.execute("INSERT OR REPLACE INTO users VALUES ('1', 'Alice', 'alice@example.com')")
    cursor.execute("INSERT OR REPLACE INTO users VALUES ('2', 'Bob', 'bob@example.com')")
    db.connection.commit()

    # Simulate web requests (these are NOT vulnerable - just for setup)
    print("=== SAFE REQUESTS (No SQL Injection) ===")

    # Login as regular user for user requests
    auth_service.login('alice', 'password')
    result1 = web_controller.handle_user_request({'user_id': '1'})
    print(f"User profile: {result1}")

    # Login as admin for admin requests
    auth_service.login('admin', 'password')  # This will fail - only alice/bob can login
    # Let's use alice as admin for demo
    auth_service.logout()
    auth_service.login('alice', 'password')  # alice is not admin, so this will fail
    try:
        result2 = web_controller.handle_admin_export({'user_id': '2'})
        print(f"Admin export: {result2}")
    except PermissionError as e:
        print(f"Admin export blocked: {e}")

if __name__ == "__main__":
    main()

# === VULNERABILITY SUMMARY ===
"""
SINGLE VULNERABILITY SINK: cursor.execute(query) in UserService.find_user_by_id()

8 ATTACK PATHS with FALSE POSITIVES:

1. attack_path_1() -> report_service.generate_user_report() -> content_service.get_user_content() -> user_service.find_user_by_id() -> cursor.execute(query)
   [4 function calls] - VULNERABLE: Direct path, no protections

2. attack_path_2() -> api_manager.api_user_profile() -> admin_service.admin_user_lookup() -> report_service.generate_user_report() -> ... -> cursor.execute(query)
   [6 function calls] - PROTECTED: Requires user authentication

3. attack_path_3() -> web_controller.handle_user_request() -> api_manager.api_user_profile() -> ... -> cursor.execute(query)
   [7 function calls] - PROTECTED: Requires user authentication

4. attack_path_4() -> user_service.find_user_by_email() -> user_service.find_user_by_id() -> cursor.execute(query)
   [3 function calls] - SANITIZED: Email validation prevents SQL injection

   attack_path_4() -> web_controller.handle_admin_export() -> ... -> cursor.execute(query)
   [8 function calls] - PROTECTED: Requires admin authentication

5. main() -> web_controller.handle_user_request() -> ... -> cursor.execute(query)
   [7 function calls] - PROTECTED: Requires user authentication

6. main() -> web_controller.handle_admin_export() -> ... -> cursor.execute(query)
   [8 function calls] - PROTECTED: Requires admin authentication

7. ContentService.search_content_by_user() -> ContentService.get_user_content() -> UserService.find_user_by_id() -> cursor.execute(query)
   [3 function calls] - DEAD CODE: This path is never called in the codebase

8. UserService.find_user_by_id_safe() - DEAD CODE: This safe method exists but is never called

FALSE POSITIVE TYPES:
- SANITIZED: Input validation prevents the attack (email regex validation)
- PROTECTED: Authentication/authorization blocks the attack
- DEAD CODE: Code paths that are never executed

ONLY ONE ACTUAL VULNERABILITY: The cursor.execute(query) call in UserService.find_user_by_id()
All protections are implemented to demonstrate false positive detection capabilities.
"""
