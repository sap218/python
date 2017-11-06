''' prac_05 exercise 1: exception handling to this code to make it more robust '''

import sys


def input_grades(grades): # 1. Use exceptions to deal with the input not being an integer here  
    try:
            print("How many names would you like to input?")
            num_names = int(sys.stdin.readline().strip())
    except ValueError:
            #while True: 
                print("Sorry, input should be numbers - how many names would you like to input?")
                num_names = int(sys.stdin.readline().strip())
           #print("Sorry, input should be numbers")
           #sys.exit(1)


    total  = 0
    for i in range(0, num_names):
      print("Input a username:")
      username = sys.stdin.readline().strip()
      grade = -1
      while grade < 0 or grade > 100: # 2. Use exceptions to deal with the input not being an integer here
         try:
             print("Input a grade:")
             grade = int(sys.stdin.readline().strip())
         except ValueError:
             print("Sorry, input should be a number - input grade:")
             grade = int(sys.stdin.readline().strip())

      # add data to dictionary
      grades[username] = grade

      # add the grade to total, to use later for average
      total += grade


   # 3. Use exceptions to make sure this is not a division by 0 here
    mean = float(total) / len(grades.keys())
    print("The mean is: " + str(mean))

def print_grades(grades):
   # Just print them all out
   for k in sorted(grades.keys()):
      print(k + " " + str(grades[k]))

def query_grades(grades):
   # Allow user to query dictionary
   stop = False
   while not stop:
      print("Which username would you like to search for?")
      uname = sys.stdin.readline().strip()
      if uname == "stop":
         stop = True
      else:
         if uname in grades:  
            print("The grade is " + str(grades[uname]))
         else:
            print("Not found: " + uname)
        

if __name__ == "__main__":
   grades = {}
   input_grades(grades)
   print_grades(grades)
