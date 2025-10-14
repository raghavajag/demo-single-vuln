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
        """Find user by email"""
        return self.find_user_by_id(email)  # Call chain: 2 functions

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

class AdminService:
    """Administrative operations"""

    def __init__(self, report_service: ReportService):
        self.report_service = report_service

    def admin_user_lookup(self, user_id: str) -> str:
        """Admin user lookup"""
        return self.report_service.generate_user_report(user_id)  # Call chain: 7 functions

    def admin_export_data(self, user_id: str) -> str:
        """Admin data export"""
        return self.report_service.export_user_data(user_id)  # Call chain: 8 functions

class APIManager:
    """API endpoint manager"""

    def __init__(self, admin_service: AdminService):
        self.admin_service = admin_service

    def api_user_profile(self, user_id: str) -> str:
        """API user profile endpoint"""
        return self.admin_service.admin_user_lookup(user_id)  # Call chain: 8 functions

    def api_admin_export(self, user_id: str) -> str:
        """API admin export endpoint"""
        return self.admin_service.admin_export_data(user_id)  # Call chain: 9 functions

class WebController:
    """Web request controller"""

    def __init__(self, api_manager: APIManager):
        self.api_manager = api_manager

    def handle_user_request(self, request_data: Dict[str, Any]) -> str:
        """Handle user profile request"""
        user_id = request_data.get('user_id', '')
        return self.api_manager.api_user_profile(user_id)  # Call chain: 9 functions

    def handle_admin_export(self, request_data: Dict[str, Any]) -> str:
        """Handle admin export request"""
        user_id = request_data.get('user_id', '')
        return self.api_manager.api_admin_export(user_id)  # Call chain: 10 functions

# === ATTACK PATH 1: Direct User Service Call ===
def attack_path_1(user_input: str) -> None:
    """Attack Path 1: 4 function calls"""
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)

    # This leads to cursor.execute(query) through 4 function calls
    report_service.generate_user_report(user_input)

# === ATTACK PATH 2: Via Admin Service ===
def attack_path_2(user_input: str) -> None:
    """Attack Path 2: 6 function calls"""
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service)
    api_manager = APIManager(admin_service)

    # This leads to cursor.execute(query) through 6 function calls
    api_manager.api_user_profile(user_input)

# === ATTACK PATH 3: Via Web Controller ===
def attack_path_3(user_input: str) -> None:
    """Attack Path 3: 5 function calls"""
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service)
    api_manager = APIManager(admin_service)
    web_controller = WebController(api_manager)

    # This leads to cursor.execute(query) through 5 function calls
    web_controller.handle_user_request({'user_id': user_input})

# === ATTACK PATH 4: Via Email Search ===
def attack_path_4(user_input: str) -> None:
    """Attack Path 4: 7 function calls"""
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service)
    api_manager = APIManager(admin_service)
    web_controller = WebController(api_manager)

    # This leads to cursor.execute(query) through 7 function calls
    # Using email search which calls find_user_by_id internally
    result = user_service.find_user_by_email(user_input)
    if result:
        web_controller.handle_admin_export({'user_id': result['id']})

# === MAIN ENTRY POINTS ===
def main():
    """Main application entry point"""
    # Initialize the full application stack
    db = DatabaseManager()
    user_service = UserService(db)
    content_service = ContentService(user_service)
    report_service = ReportService(content_service)
    admin_service = AdminService(report_service)
    api_manager = APIManager(admin_service)
    web_controller = WebController(api_manager)

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
    result1 = web_controller.handle_user_request({'user_id': '1'})
    print(f"User profile: {result1}")

    result2 = web_controller.handle_admin_export({'user_id': '2'})
    print(f"Admin export: {result2}")

if __name__ == "__main__":
    main()

# === VULNERABILITY SUMMARY ===
"""
SINGLE VULNERABILITY SINK: cursor.execute(query) in UserService.find_user_by_id()

4 ATTACK PATHS (4-6+ chained function calls):

1. attack_path_1() -> report_service.generate_user_report() -> content_service.get_user_content() -> user_service.find_user_by_id() -> cursor.execute(query)
   [4 function calls to vulnerable sink]

2. attack_path_2() -> api_manager.api_user_profile() -> admin_service.admin_user_lookup() -> report_service.generate_user_report() -> ... -> cursor.execute(query)
   [6 function calls to vulnerable sink]

3. attack_path_3() -> web_controller.handle_user_request() -> api_manager.api_user_profile() -> ... -> cursor.execute(query)
   [5 function calls to vulnerable sink]

4. attack_path_4() -> web_controller.handle_admin_export() -> api_manager.api_admin_export() -> ... -> cursor.execute(query)
   [7 function calls to vulnerable sink]

ONLY ONE ACTUAL VULNERABILITY: The cursor.execute(query) call in UserService.find_user_by_id()
All other calls to the same method are through safe, parameterized paths.
"""
