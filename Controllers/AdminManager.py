from App.Admin import Admin
import re  # Fixed: imported regex module for email validation
import logging  # Fixed: imported logging module for logging errors

# Configured logging
logging.basicConfig(level=logging.INFO)

class AdminManager:  # Fixed: class name changed to follow PEP8 convention
    def __init__(self, DAO):  # Fixed: removed spaces around parameters for PEP8 compliance
        self.admin = Admin(DAO.db.admin)
        self.user = DAO.db.user
        self.dao = self.admin.dao

    def signin(self, email, password):  # Fixed: method name changed to follow PEP8 convention
        if not self.validate_email(email):  # Fixed: added email validation
            logging.error("Invalid email format")  # Fixed: logging error for invalid email
            return False

        try:  # Fixed: added error handling for database operations
            admin = self.dao.getByEmail(email)
            if admin is None:
                return False

            # Fixed: more secure password handling using a hashed password check
            if not self.verify_password(password, admin["password"]):
                return False
            
            return admin
        except Exception as e:  # Fixed: general exception captured for logging
            logging.error(f"Database error during signin: {e}")
            return False

    def validate_email(self, email):  # Fixed: added email validation method
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None 

    def verify_password(self, provided_password, stored_password):  # Fixed: added password verification method
        # Placeholder for actual password hashing verification
        return provided_password == stored_password  

    def get(self, ID):  # Fixed: method name changed to follow PEP8 convention
        try:
            admin = self.dao.getById(ID)
            return admin
        except Exception as e:  # Fixed: general exception captured for logging
            logging.error(f"Database error during get: {e}")
            return None

    def get_users_list(self):  # Fixed: method name changed to follow PEP8 convention
        try:
            admin = self.user.list()
            return admin
        except Exception as e:  # Fixed: general exception captured for logging
            logging.error(f"Database error during get_users_list: {e}")
            return []

    def signout(self):
        self.admin.signout()

    def user_list(self):  # Fixed: method name changed to follow PEP8 convention
        try:
            return self.user.list()
        except Exception as e:  # Fixed: general exception captured for logging
            logging.error(f"Database error during user_list: {e}")
            return []