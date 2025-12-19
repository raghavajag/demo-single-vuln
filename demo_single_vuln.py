AWS_ACCESS_KEY_ID=AKIA0DUMMYACCESSKEY1234
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYDUMMYSECRET
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET_NAME=prod-app-bucket


S3_BUCKET_NAME=prod-app-bucket
sk-proj-abcdefghij1234567890T3BlbkFJklmnopqrstuv0987654321

sk-proj-Xk9Lm2NpQr4StVwYz1AbT3BlbkFJCdEfGhIj3KlMnOpQrStU

sk-proj-7HjKlMnBvCx4ZaQwErTyT3BlbkFJUiOpAsDfGhJkL9mNbVcX

sk-proj-Qw3rTyU8pLkJhGfDsAzXT3BlbkFJcVbNm7KjHgFdSaPo1LkJ

sk-proj-9TgBnHyU3mJkLpQrStVwT3BlbkFJXyZ1aBcDeFgHiJkLmNoP

sk-proj-Lm8nBvCxZaQwErTyUiOpT3BlbkFJ3SdFgHjKl6MnBvCxZaQw


DB_CONNECTION=postgres
DB_HOST=prod-db.cluster-abc123.us-east-1.rds.amazonaws.com
DB_PORT=5432
DB_DATABASE=customer_db
DB_USERNAME=crm_admin
DB_PASSWORD=Str0ngP@ssw0rd!123
AWS_ACCESS_KEY_ID=AKIAZ3FXJW9KPQR2HVBN
AWS_SECRET_ACCESS_KEY=7hGnU9pQrStVwXyZ1234AbCdEfGhIjKlMnOpQrSt

 AWS_ACCESS_KEY_ID=AKIAZ3FXJW9KPQR2HVBN
AWS_SECRET_ACCESS_KEY=7hGnU9pQrStVwXyZ1234AbCdEfGhIjKlMnOpQrSt

AWS_ACCESS_KEY_ID=AKIAJH6QCZVF4TNMLW9R
AWS_SECRET_ACCESS_KEY=Kf3xR9mNpL2qWvYz8bJc4dHgTnSaEiUo6wXrCyPm

AWS_ACCESS_KEY_ID=AKIAVB8NXWMK2PRT5YQZ
AWS_SECRET_ACCESS_KEY=pN4rTgHj7KmLqWsXyZ9v2CbDfGhJkMnPrStUvWxY

AWS_ACCESS_KEY_ID=AKIAQM4LGTRZ7WXN9YCP
AWS_SECRET_ACCESS_KEY=Lm8nBvCxZaQwErTyUiOp3SdFgHjKl6MnBvCxZaQw

AWS_ACCESS_KEY_ID=AKIAXK5HNWPV2QR8JTZM
AWS_SECRET_ACCESS_KEY=9TgBnHyU3mJkLpQrStVwXyZ1aBcDeFgHiJkLmNoP

AWS_ACCESS_KEY_ID=AKIARF9PMZWL4VXT6NBQ
AWS_SECRET_ACCESS_KEY=WqErTyU8pLkJhGfDsAzXcVbNm3QwErTyUiOpAsDf

AWS_ACCESS_KEY_ID=AKIABM7KCNQZ3PXJW5VR
AWS_SECRET_ACCESS_KEY=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

AWS_ACCESS_KEY_ID=AKIAZP2RNTXK8WLVM6QJ
AWS_SECRET_ACCESS_KEY=5YtReDsWqAzXcVbNm7KjHgFdSaPo1LkJhGfDsAzX

AWS_ACCESS_KEY_ID=AKIALW6XQJNVK9PRT3ZM
AWS_SECRET_ACCESS_KEY=CvBnMkLpOiUyTrEwQ8sAdFgHjKlZxCvBnMaQwErT

AWS_ACCESS_KEY_ID=AKIAHC4VNBQZ7XWKM9PJ
AWS_SECRET_ACCESS_KEY=QwErTyUiOp2AsDfGhJkLzXcVbNm6MkLpOiUyTrEw


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

"""
Demo Multi-Vulnerability Testing File
=====================================

Three Vulnerabilities with Multiple Attack Paths Each:
1. SQL Injection in cursor.execute(query) - UserService.find_user_by_id
2. SSTI in render_template_string() - TemplateService.render_user_template  
3. SQL Injection in cursor.execute(query) - AnalyticsService.get_user_stats

Each vulnerability has 4-8 attack paths demonstrating:
- VULNERABLE paths (exploitable)
- PROTECTED paths (auth/authz controls)
- SANITIZED paths (input validation)
- DEAD CODE paths (unreachable)
"""

import sqlite3
import logging
from typing import Optional, Dict, Any, List
from flask import render_template_string  # For SSTI vulnerability

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

class AuthService:
    """Authentication and authorization service"""

    def __init__(self):
        self.current_user = None
        self.admin_users = ['admin', 'superuser']

    def login(self, username: str, password: str) -> bool:
        """Simple login - for demo purposes"""
        if username in ['alice', 'bob', 'admin'] and password == 'password':
            self.current_user = username
            return True
        return False

    def logout(self):
        """Logout current user"""
        self.current_user = None

    def is_admin(self) -> bool:
        """Check if current user is admin"""
        return self.current_user in self.admin_users

    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.current_user is not None

# ============================================================================
# VULNERABILITY 1: SQL INJECTION in UserService.find_user_by_id
# ============================================================================

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

    def find_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Find user by email - SANITIZED (validates email format)"""
        import re
        # Email validation prevents SQL injection
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return None
        # Even though this calls find_user_by_id, the email validation sanitizes input
        return self.find_user_by_id(email)

class UserProfileService:
    """User profile operations"""

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user profile"""
        return self.user_service.find_user_by_id(user_id)

    def get_profile_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get profile by email - calls sanitized path"""
        return self.user_service.find_user_by_email(email)

class UserReportService:
    """User report generation"""

    def __init__(self, profile_service: UserProfileService):
        self.profile_service = profile_service

    def generate_report(self, user_id: str) -> str:
        """Generate user report"""
        user = self.profile_service.get_profile(user_id)
        if user:
            return f"Report for {user['name']}"
        return "User not found"

# ============================================================================
# VULNERABILITY 2: SSTI in TemplateService.render_user_template
# ============================================================================

class TemplateService:
    """Template rendering service - Contains VULN 2"""

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def render_user_template(self, template_str: str) -> str:
        """Render user template - VULNERABLE SINK #2"""
        # VULN 2: SSTI (Server-Side Template Injection)
        return render_template_string(template_str)  # Dangerous!

    def render_safe_template(self, user_id: str) -> str:
        """Render template with sanitized input"""
        # Sanitize by using predefined template
        template = "<h1>User Profile</h1><p>ID: {{ user_id }}</p>"
        return render_template_string(template, user_id=user_id)

class EmailService:
    """Email generation service"""

    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def generate_email(self, template: str) -> str:
        """Generate email from template"""
        return self.template_service.render_user_template(template)

    def generate_welcome_email(self, username: str) -> str:
        """Generate welcome email - SANITIZED"""
        # Uses safe template with escaping
        safe_template = "<h1>Welcome!</h1><p>Hello {{ username }}</p>"
        return render_template_string(safe_template, username=username)

class NotificationService:
    """Notification service"""

    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def send_notification(self, template: str) -> str:
        """Send notification"""
        return self.email_service.generate_email(template)

    def send_custom_notification(self, message: str) -> str:
        """Send custom notification"""
        template = f"<div>{message}</div>"
        return self.send_notification(template)

class MarketingService:
    """Marketing campaign service"""

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_campaign(self, campaign_template: str) -> str:
        """Send marketing campaign"""
        return self.notification_service.send_notification(campaign_template)

    def send_personalized_campaign(self, user_id: str, template: str) -> str:
        """Send personalized campaign"""
        return self.send_campaign(template)

# ============================================================================
# VULNERABILITY 3: SQL INJECTION in AnalyticsService.get_user_stats
# ============================================================================

class AnalyticsService:
    """Analytics service - Contains VULN 3"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def get_user_stats(self, user_filter: str) -> List[Dict[str, Any]]:
        """Get user statistics - VULNERABLE SINK #3"""
        cursor = self.db_manager.get_cursor()
        query = f"SELECT user_id, COUNT(*) as count FROM events WHERE user_id LIKE '%{user_filter}%' GROUP BY user_id"
        cursor.execute(query)  # VULN 3: SQL INJECTION SINK
        results = cursor.fetchall()
        return [dict(zip(['user_id', 'count'], row)) for row in results]

    def get_user_stats_safe(self, user_filter: str) -> List[Dict[str, Any]]:
        """Get user statistics with sanitization"""
        # Sanitize input - only alphanumeric
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', user_filter):
            return []
        return self.get_user_stats(user_filter)

class ReportingService:
    """Reporting service"""

    def __init__(self, analytics_service: AnalyticsService):
        self.analytics_service = analytics_service

    def generate_stats_report(self, filter_criteria: str) -> List[Dict[str, Any]]:
        """Generate statistics report"""
        return self.analytics_service.get_user_stats(filter_criteria)

    def generate_safe_stats_report(self, filter_criteria: str) -> List[Dict[str, Any]]:
        """Generate safe statistics report"""
        return self.analytics_service.get_user_stats_safe(filter_criteria)

class DashboardService:
    """Dashboard service"""

    def __init__(self, reporting_service: ReportingService):
        self.reporting_service = reporting_service

    def get_dashboard_data(self, filter_str: str) -> List[Dict[str, Any]]:
        """Get dashboard data"""
        return self.reporting_service.generate_stats_report(filter_str)

    def get_filtered_dashboard(self, filter_str: str) -> List[Dict[str, Any]]:
        """Get filtered dashboard with sanitization"""
        return self.reporting_service.generate_safe_stats_report(filter_str)

# ============================================================================
# PROTECTED PATHS - Authentication/Authorization Wrappers
# ============================================================================

class ProtectedUserAPI:
    """Protected user API - requires authentication"""

    def __init__(self, report_service: UserReportService, auth_service: AuthService):
        self.report_service = report_service
        self.auth_service = auth_service

    def get_user_report(self, user_id: str) -> str:
        """Get user report - PROTECTED by authentication"""
        if not self.auth_service.is_authenticated():
            raise PermissionError("Authentication required")
        return self.report_service.generate_report(user_id)

class AdminAPI:
    """Admin API - requires admin privileges"""

    def __init__(self, dashboard_service: DashboardService, auth_service: AuthService):
        self.dashboard_service = dashboard_service
        self.auth_service = auth_service

    def get_admin_dashboard(self, filter_str: str) -> List[Dict[str, Any]]:
        """Get admin dashboard - PROTECTED by admin check"""
        if not self.auth_service.is_admin():
            raise PermissionError("Admin privileges required")
        return self.dashboard_service.get_dashboard_data(filter_str)

class ProtectedMarketingAPI:
    """Protected marketing API"""

    def __init__(self, marketing_service: MarketingService, auth_service: AuthService):
        self.marketing_service = marketing_service
        self.auth_service = auth_service

    def send_admin_campaign(self, template: str) -> str:
        """Send admin campaign - PROTECTED"""
        if not self.auth_service.is_admin():
            raise PermissionError("Admin privileges required")
        return self.marketing_service.send_campaign(template)

# ============================================================================
# DEAD CODE - Never called in execution
# ============================================================================

class UnusedLegacyService:
    """Legacy service that is never instantiated or called - DEAD CODE"""

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def legacy_user_lookup(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Legacy method - never called"""
        return self.user_service.find_user_by_id(user_id)

class DeadTemplateService:
    """Template service that is never used - DEAD CODE"""

    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def render_legacy_template(self, template: str) -> str:
        """Legacy template rendering - never called"""
        return self.template_service.render_user_template(template)

class UnusedAnalyticsService:
    """Analytics service that is never used - DEAD CODE"""

    def __init__(self, analytics_service: AnalyticsService):
        self.analytics_service = analytics_service

    def get_legacy_stats(self, filter_str: str) -> List[Dict[str, Any]]:
        """Legacy stats - never called"""
        return self.analytics_service.get_user_stats(filter_str)

# ============================================================================
# ATTACK PATH ENTRY POINTS
# ============================================================================

def attack_path_sql_1(user_input: str):
    """VULN 1 - Path 1: Direct vulnerable SQL injection (4 hops) - VULNERABLE"""
    db = DatabaseManager()
    user_service = UserService(db)
    profile_service = UserProfileService(user_service)
    report_service = UserReportService(profile_service)
    # 4 hops: report_service -> profile_service -> user_service -> cursor.execute
    report_service.generate_report(user_input)

def attack_path_sql_2(user_input: str):
    """VULN 1 - Path 2: Protected SQL injection (6 hops) - PROTECTED"""
    db = DatabaseManager()
    auth = AuthService()
    user_service = UserService(db)
    profile_service = UserProfileService(user_service)
    report_service = UserReportService(profile_service)
    protected_api = ProtectedUserAPI(report_service, auth)
    # 6 hops but PROTECTED by auth check
    protected_api.get_user_report(user_input)

def attack_path_sql_3(email_input: str):
    """VULN 1 - Path 3: Sanitized SQL injection (4 hops) - SANITIZED"""
    db = DatabaseManager()
    user_service = UserService(db)
    profile_service = UserProfileService(user_service)
    # 4 hops but SANITIZED by email validation
    profile_service.get_profile_by_email(email_input)

def attack_path_ssti_1(template_input: str):
    """VULN 2 - Path 1: Direct SSTI (5 hops) - VULNERABLE"""
    db = DatabaseManager()
    user_service = UserService(db)
    template_service = TemplateService(user_service)
    email_service = EmailService(template_service)
    notification_service = NotificationService(email_service)
    # 5 hops: notification -> email -> template -> render_template_string
    notification_service.send_notification(template_input)

def attack_path_ssti_2(template_input: str):
    """VULN 2 - Path 2: SSTI via marketing (7 hops) - VULNERABLE"""
    db = DatabaseManager()
    user_service = UserService(db)
    template_service = TemplateService(user_service)
    email_service = EmailService(template_service)
    notification_service = NotificationService(email_service)
    marketing_service = MarketingService(notification_service)
    # 7 hops: marketing -> notification -> email -> template -> render_template_string
    marketing_service.send_campaign(template_input)

def attack_path_ssti_3(template_input: str):
    """VULN 2 - Path 3: Protected SSTI (8 hops) - PROTECTED"""
    db = DatabaseManager()
    auth = AuthService()
    user_service = UserService(db)
    template_service = TemplateService(user_service)
    email_service = EmailService(template_service)
    notification_service = NotificationService(email_service)
    marketing_service = MarketingService(notification_service)
    protected_marketing = ProtectedMarketingAPI(marketing_service, auth)
    # 8 hops but PROTECTED by admin check
    protected_marketing.send_admin_campaign(template_input)

def attack_path_analytics_1(filter_input: str):
    """VULN 3 - Path 1: Direct analytics SQL injection (4 hops) - VULNERABLE"""
    db = DatabaseManager()
    analytics_service = AnalyticsService(db)
    reporting_service = ReportingService(analytics_service)
    dashboard_service = DashboardService(reporting_service)
    # 4 hops: dashboard -> reporting -> analytics -> cursor.execute
    dashboard_service.get_dashboard_data(filter_input)

def attack_path_analytics_2(filter_input: str):
    """VULN 3 - Path 2: Protected analytics (6 hops) - PROTECTED"""
    db = DatabaseManager()
    auth = AuthService()
    analytics_service = AnalyticsService(db)
    reporting_service = ReportingService(analytics_service)
    dashboard_service = DashboardService(reporting_service)
    admin_api = AdminAPI(dashboard_service, auth)
    # 6 hops but PROTECTED by admin check
    admin_api.get_admin_dashboard(filter_input)

def attack_path_analytics_3(filter_input: str):
    """VULN 3 - Path 3: Sanitized analytics (5 hops) - SANITIZED"""
    db = DatabaseManager()
    analytics_service = AnalyticsService(db)
    reporting_service = ReportingService(analytics_service)
    dashboard_service = DashboardService(reporting_service)
    # 5 hops but SANITIZED by input validation
    dashboard_service.get_filtered_dashboard(filter_input)

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main application entry point"""
    db = DatabaseManager()
    auth = AuthService()

    # Setup database
    cursor = db.get_cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            user_id TEXT,
            event_type TEXT,
            timestamp INTEGER
        )
    """)
    cursor.execute("INSERT OR REPLACE INTO users VALUES ('1', 'Alice', 'alice@example.com')")
    cursor.execute("INSERT OR REPLACE INTO users VALUES ('2', 'Bob', 'bob@example.com')")
    cursor.execute("INSERT INTO events VALUES ('1', 'login', 1234567890)")
    cursor.execute("INSERT INTO events VALUES ('2', 'click', 1234567891)")
    db.connection.commit()

    print("=== Demo Application Initialized ===")
    print("3 Vulnerabilities with Multiple Attack Paths Ready for Testing")

if __name__ == "__main__":
    main()

# ============================================================================
# VULNERABILITY SUMMARY
# ============================================================================
"""
THREE VULNERABILITIES FOR SCANNER TESTING:

═══════════════════════════════════════════════════════════════════════════
VULNERABILITY 1: SQL INJECTION in UserService.find_user_by_id()
═══════════════════════════════════════════════════════════════════════════
SINK: cursor.execute(query) at line ~79

ATTACK PATHS:
1. attack_path_sql_1() [4 hops] - VULNERABLE
   └─> UserReportService.generate_report()
       └─> UserProfileService.get_profile()
           └─> UserService.find_user_by_id()
               └─> cursor.execute(query) ⚠️ VULNERABLE

2. attack_path_sql_2() [6 hops] - PROTECTED (authentication required)
   └─> ProtectedUserAPI.get_user_report() 🛡️ AUTH CHECK
       └─> UserReportService.generate_report()
           └─> UserProfileService.get_profile()
               └─> UserService.find_user_by_id()
                   └─> cursor.execute(query)

3. attack_path_sql_3() [4 hops] - SANITIZED (email validation)
   └─> UserProfileService.get_profile_by_email()
       └─> UserService.find_user_by_email() 🧹 EMAIL REGEX VALIDATION
           └─> UserService.find_user_by_id()
               └─> cursor.execute(query)

4. UnusedLegacyService.legacy_user_lookup() - DEAD CODE ☠️
   └─> Never instantiated or called

═══════════════════════════════════════════════════════════════════════════
VULNERABILITY 2: SSTI in TemplateService.render_user_template()
═══════════════════════════════════════════════════════════════════════════
SINK: render_template_string(template_str) at line ~107

ATTACK PATHS:
1. attack_path_ssti_1() [5 hops] - VULNERABLE
   └─> NotificationService.send_notification()
       └─> EmailService.generate_email()
           └─> TemplateService.render_user_template()
               └─> render_template_string(template_str) ⚠️ VULNERABLE

2. attack_path_ssti_2() [7 hops] - VULNERABLE
   └─> MarketingService.send_campaign()
       └─> NotificationService.send_notification()
           └─> EmailService.generate_email()
               └─> TemplateService.render_user_template()
                   └─> render_template_string(template_str) ⚠️ VULNERABLE

3. attack_path_ssti_3() [8 hops] - PROTECTED (admin privileges required)
   └─> ProtectedMarketingAPI.send_admin_campaign() 🛡️ ADMIN CHECK
       └─> MarketingService.send_campaign()
           └─> NotificationService.send_notification()
               └─> EmailService.generate_email()
                   └─> TemplateService.render_user_template()
                       └─> render_template_string(template_str)

4. EmailService.generate_welcome_email() [1 hop] - SANITIZED
   └─> Uses safe template with proper escaping 🧹 SAFE TEMPLATE

5. DeadTemplateService.render_legacy_template() - DEAD CODE ☠️
   └─> Never instantiated or called

═══════════════════════════════════════════════════════════════════════════
VULNERABILITY 3: SQL INJECTION in AnalyticsService.get_user_stats()
═══════════════════════════════════════════════════════════════════════════
SINK: cursor.execute(query) at line ~163

ATTACK PATHS:
1. attack_path_analytics_1() [4 hops] - VULNERABLE
   └─> DashboardService.get_dashboard_data()
       └─> ReportingService.generate_stats_report()
           └─> AnalyticsService.get_user_stats()
               └─> cursor.execute(query) ⚠️ VULNERABLE

2. attack_path_analytics_2() [6 hops] - PROTECTED (admin privileges required)
   └─> AdminAPI.get_admin_dashboard() 🛡️ ADMIN CHECK
       └─> DashboardService.get_dashboard_data()
           └─> ReportingService.generate_stats_report()
               └─> AnalyticsService.get_user_stats()
                   └─> cursor.execute(query)

3. attack_path_analytics_3() [5 hops] - SANITIZED (alphanumeric validation)
   └─> DashboardService.get_filtered_dashboard()
       └─> ReportingService.generate_safe_stats_report()
           └─> AnalyticsService.get_user_stats_safe() 🧹 REGEX VALIDATION
               └─> AnalyticsService.get_user_stats()
                   └─> cursor.execute(query)

4. UnusedAnalyticsService.get_legacy_stats() - DEAD CODE ☠️
   └─> Never instantiated or called

═══════════════════════════════════════════════════════════════════════════
SCANNER TEST OBJECTIVES:
═══════════════════════════════════════════════════════════════════════════
✓ Detect all 3 vulnerable sinks
✓ Trace all attack paths with complex call chains (4-8 hops)
✓ Identify FALSE POSITIVES:
  - PROTECTED paths (authentication/authorization controls)
  - SANITIZED paths (input validation/escaping)
  - DEAD CODE paths (unreachable code)
✓ Classify paths correctly using LLM analysis
✓ Generate comprehensive reports for each vulnerability

TOTAL: 3 Vulnerabilities, ~12 Attack Paths (mix of VULNERABLE, PROTECTED, SANITIZED, DEAD CODE)
"""
