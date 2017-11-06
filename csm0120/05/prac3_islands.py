''' prac_05 exercise 2: add comments and/or docstrings to this code '''
''' summary what function does, description of parameters that function takes, description of what function returns (if anything) '''
''' Use pydoc to produce a webpage of documentation for this module '''

import math

# function 1
def land_rectangle_area(x1, y1, x2, y2):
   """ calculating the area of land as a rectangle 
   takes in parameters of co-ordinates from an island
   function returns the answer: absolute value - the (positive) distance between the two numbers
   """
   return ( abs(x2-x1) * abs(y2-y1) )

#function 2
def land_circle_area(x1, y1, x2, y2):
   """ calculating circle area of land
   takes in co-ordintates as parameters
   returns the area
   """
   radius = math.sqrt((x2-x1)**2 + (y2-y1)**2)
   return ( math.pi * radius * radius )

#function 3
def difference_area(x1, y1, x2, y2):
   """ finding the area from the co-ordinates of the island
   returns the circle area subtracting the land area
   """
   r = land_rectangle_area(x1, y1, x2, y2) # function 1 called
   c = land_circle_area(x1, y1, x2, y2) # function 2 called
   return (c - r)

#function 4
def smallest_island(islands):
  """ takes in parameters of the islands and finds the co-ordinates
  calculates the area of each island and returns the smallest
  """
  min_area = 1000000  # can debate if this is a sensible default value
  smallest = ""
  for i in islands:
    coords = islands[i]
    size = land_rectangle_area(coords[0],coords[1],coords[2],coords[3]) # function 1 called
    if size < min_area:
      min_area = size
      smallest = i
  return smallest


def main():
   islands = {
     "Banana island"    : (3,5,7,6),
     "Mango island"     : (10,3,19,4),
     "Pineapple island" : (8,8,9,20),
     "Coconut island"   : (2,13,5,9),
     "Peach island"     : (1,3,4,2)
     }
   s = smallest_island(islands) # function 4 called
   print(s)
   d = difference_area(islands[s][0],islands[s][1],islands[s][2],islands[s][3]) # function 3 called
   print(d)
   

if __name__ == "__main__":
   main()
