import urllib.request


def auth_use():
  # 1. user name and password
  user = "admin"
  pwd = "admin123"
  url = "http://192.168.179.66"
  
  # 2. create pwd_manager
  pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
  
  pwd_manager.add_password(None, url, user, pwd)
  
  # 3. create auth_handler
  auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)
  
  opener = urllib.request.build_opener(auth_handler)
  
  response = opener.open(url)
  
auth_use()
