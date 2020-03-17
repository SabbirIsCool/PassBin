from OpenPassFN import *

#Intro
print("Hello, user!")
print("Welcome to the OpenPass!")
print("Your Personal Password Generator!")
Line()

# Information Input

### Password Count
print("How many password(s) you want?")
Pass_Count = input("Answer: ")
### Password Digits
print("How many digit(s) you want?")
Pass_Digit = input("Answer: ")

# Information Processing and Output
Line()
### Integer Detection
Pass_Count_Detect = intDetect(Pass_Count)
Pass_Digit_Detect = intDetect(Pass_Digit)

if Pass_Count_Detect and Pass_Digit_Detect:
  SecPassGen(Pass_Count, Pass_Digit)
else:
  print("The inputed information(s) is NOT number(s)!")
  print("Please type integers next time.")

# Credits
Line()
print("Created by: Sabbir Hossain")

# Exit Prompt
Line()
Exit = input("(Press Enter key to exit) \n \n")
