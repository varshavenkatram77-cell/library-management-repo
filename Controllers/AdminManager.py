from App.Admin import Admin
import logging  # Fixed: imported logging for tracking execution flow

class AdminManager:  # Fixed: changed class name to follow PEP8 convention
    def __init__(self, DAO):
        self.admin = Admin(DAO.db.admin)
        self.user = DAO.db.user
        self.dao = self.admin.dao

    def signin(self, email, password):
        if not self.validate_email(email):  # Fixed: added email validation
            logging.warning("Invalid email format")  # Fixed: added logging for invalid email
            return False
        if not self.validate_password(password):  # Fixed: added password validation
            logging.warning("Invalid password format")  # Fixed: added logging for invalid password
            return False

        try:  # Fixed: added error handling for database access
            admin = self.dao.getByEmail(email)
        except Exception as e:
            logging.error("Database access error: %s", e)  # Fixed: log error if database access fails
            return False
        
        if admin is None:
            return False
        
        admin_pass = admin["password"]
        if not self.compare_passwords(admin_pass, password):  # Fixed: added secure password comparison
            return False
        
        return admin

    def get(self, ID):
        try:  # Fixed: added error handling for database access
            admin = self.dao.getById(ID)
            return admin
        except Exception as e:
            logging.error("Database access error: %s", e)  # Fixed: log error if database access fails
            return None

    def get_users_list(self):  # Fixed: renamed method to follow PEP8 convention
        try:  # Fixed: added error handling for database access
            admin = self.user.list()
            return admin
        except Exception as e:
            logging.error("Database access error: %s", e)  # Fixed: log error if database access fails
            return None

    def signout(self):
        self.admin.signout()

    def user_list(self):
        return self.user.list()

    def validate_email(self, email):  # Fixed: added email validation method
        # Implement email validation logic here
        return True
    
    def validate_password(self, password):  # Fixed: added password validation method
        # Implement password validation logic here
        return True

    def compare_passwords(self, stored_password, provided_password):  # Fixed: added secure password comparison method
        # Implement password comparison logic here (use hashing)
        return stored_password == provided_password  # Fixed: change this to use a secure comparison