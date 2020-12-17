class Traveller:
   '''Class Name
      Attributes: first name, nickname, last name
      Methods: 
   '''

   def __init__(self, first_name, last_name, username, password, account_email):
      self.first_name = first_name
      self.last_name = last_name
      self.username = username
      self.password = password
      self.email = account_email

   def get_fullname(self):
      return self.first_name + " " + self.last_name
   
   def get_first_name(self):
      return self.first_name
   
   def get_last_name(self):
      return self.last_name

   def get_username(self):
      return self.username
   
   def get_password(self):
      return self.password
   
   def get_email(self):
      return self.email

   def change_password(self, password):
      self.password = password
      
   def change_email(self, account_email):   
      self.email = account_email 