from App.Admin import Admin
import bcrypt  # Fixed: imported bcrypt for password hashing
import logging  # Fixed: imported logging for better tracking of events

logging.basicConfig(level=logging.INFO)  # Fixed: configured logging

class AdminManager:  # Fixed: renamed class to adhere to PEP8 convention
    def __init__(self, DAO):
        self.admin = Admin(DAO.db.admin)
        self.user = DAO.db.user
        self.dao = self.admin.dao

    def signin(self, email, password):  # Fixed: clarified spacing
        if not isinstance(email, str) or not isinstance(password, str):  # Fixed: added input validation
            raise ValueError("Invalid input types for email or password")  # Fixed: raised ValueError for invalid input types
        
        admin = self.dao.getByEmail(email)
        if admin is None:  # Fixed: changed to more pythonic form
            return {"success": False, "message": "Admin not found"}  # Fixed: improved return message
        admin_pass = admin["password"].encode('utf-8')  # Fixed: encode stored password
        if not bcrypt.checkpw(password.encode('utf-8'), admin_pass):  # Fixed: used bcrypt to check hashed password
            return {"success": False, "message": "Invalid password"}  # Fixed: improved return message
        logging.info(f"Admin {email} signed in successfully")  # Fixed: added logging for successful sign-in
        return {"success": True, "admin": admin}  # Fixed: structured return with success status

    def get(self, ID):  # Fixed: clarified spacing
        if not isinstance(ID, int):  # Fixed: added input validation for ID
            raise ValueError("ID must be an integer")  # Fixed: raised ValueError for invalid ID
        admin = self.dao.getById(ID)
        return admin

    def getUsersList(self):
        users = self.user.list()  # Fixed: renamed variable for clarity
        logging.info(f"Retrieved users list: {users}")  # Fixed: added logging
        return users

    def signout(self):
        self.admin.signout()
        logging.info("Admin signed out")  # Fixed: added logging for sign out

    def get_user_list(self):  # Fixed: renamed method for clarity and conformity
        users = self.user.list()  # Fixed: renamed variable for clarity
        return users  # Fixed: added return since method is renamed