# Main Algorithms

# Line Function
def Line():
  print("------------------------------------------")

# IntDetect Function
def intDetect(x):
  IsInt = True
  x_copy = x
  try:
    x_copy = int(x)
  except ValueError:
    IsInt = False
  return IsInt

# SecPassGen Algorithm
def SecPassGen(Pass_Count, Pass_Digit):
  import random
  import string
  
  Pass_Count = int(Pass_Count)
  Pass_Digit = int(Pass_Digit)
  CharVar = string.ascii_letters + string.digits + '!@#$%^&*()'

  for i in range(Pass_Count):
    GenPass = ''.join(random.choice(CharVar) for h in range(Pass_Digit))

    print("Password: " + GenPass)
