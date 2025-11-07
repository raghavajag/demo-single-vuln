class UserService:
    """User management service - Contains VULN 1"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def find_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Find user by ID - VULNERABLE SINK #1"""
        cursor = self.db_manager.get_cursor()
        query = f"SELECT * FROM users WHERE id = '{user_id}'"  # SQL Injection
        cursor.execute(query)  # VULN 1: SQL INJECTION SINK
        result = cursor.fetchone()
        return dict(zip(['id', 'name', 'email'], result)) if result else None
