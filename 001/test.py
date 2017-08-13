# Created on Sat Jul 29 15:30:44 2017

# @author: Sam

name = "Sam"
letter = "SAM"[0]
print (name.upper(), "is", len(name), "letters long - first letter is:", letter.lower())
pi = 3.14
print (str(pi), pi)
print()

########################

var1 = 3
var2 = 4
var3 = var1 ** var2

print ("var1 =", var1)
print ("var2 =", var2)
print ("var1 + var2 =", var1 + var2)
print ("var1 - var2 =", var1 - var2)
print ("var1 * var2 =", var1 * var2)
print ("var1 / var2 =", var1 / var2)
print ("var1^var2 =", var3)
print ("Modulo: var2 % var1 =", var2 % var1)

var1 = 8
print ("new var1 =", var1, "--- var1 + var2 =", var1 + var2)
print ()

###########################

#name = raw_input("What is your name?")
#quest = raw_input("What is your quest?")
#color = raw_input("What is your favorite color?")

#print ("Ah, so your name is %s, your quest is %s, " \
#"and your favorite color is %s." % (name, quest, color))
print ()

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)