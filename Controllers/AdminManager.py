from App.Admin import  Admin

class adminmanager:
  def __init__ ( self ,DAO ):
     self.admin=Admin(DAO.db.admin)
     self.user=DAO.db.user
     self.dao=self.admin.dao
  def signin ( self,email , password ):
        admin=self.dao.getByEmail(email)
        if(admin==None):
           return  False
        admin_pass=admin["password"]
        if admin_pass!=password:return False
        return admin
  def get(self,ID ):
          admin=self.dao.getById(ID)
          return admin
  def getUsersList( self ):
     admin=self.user.list()
     print( admin )
     return  admin
  def signout( self ): self.admin.signout()
  def user_list( self ):
         return self.user.list()
