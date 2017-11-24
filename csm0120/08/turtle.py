import math
#import matplotlib.pyplot as plt

class Turtle:
    #theta = 0.2
    #x = 0
    #y = 0
    #direction = 0

    def __init__ (self,x=0,y=0):
        self.theta = 0.2
        self.x = 0
        self.y = 0
        self.direction = 0

    def forward(self):
        self.x = self.x + math.cos(self.direction)
        self.y = self.y + math.sin(self.direction)

    def turn_right(self):
        self.direction = (self.direction - self.theta) % (2*math.pi)

    def turn_left(self):
        self.direction = (self.direction + self.theta) % (2*math.pi)

if __name__ == "__main__":
    
    t1 = Turtle(3,1)
    t2 = Turtle(x=5,y=0)
    
    print("t1 start: ", t1.x, t1.y)   
    t1.forward()
    t1.forward()
    t1.forward()
    t1.forward()
    t1.forward()
    t1.turn_left()
    t1.forward()
    t1.forward()
    print("t1 end: ", t1.x, t1.y)
    #plt.plot(t1.x, t1.y)

    print("t2 start: ", t2.x, t2.y)
    t2.forward()
    t2.turn_right()
    t2.forward()
    t2.forward()
    t2.forward()
    t2.forward()
    t2.forward()
    t2.forward()
    t2.forward()
    print("t2 end: ", t2.x, t2.y)
    