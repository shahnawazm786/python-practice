def is_valid_username(name):
   if not name:
       return False
   if name.lower() == name.upper():
       return False
   if name == name[::-1]:
       return False
   if ord(name[0]) % 2 == 0:
       return True
   return False

print(is_valid_username("Bob"))