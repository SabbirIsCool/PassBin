def SecPassGen(Pass_Count, Pass_Digit):
  import random
  import string
  
  CharVar = string.ascii_letters + string.digits + '!@#$%^&*()'
  
  for i in range(Pass_Count):
    GenPass = ''.join(random.choice(CharVar) for h in range(Pass_Digit))
    print("Password: " + GenPass)
