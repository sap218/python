# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:10:04 2017 | @author: sap21
> Recreation of my script
"""

#USING EXAM SCORE FOR EXAMPLE

num_array = list()
num = input("enter number of exams:")
print ('enter score in set: ')
for i in range(int(num)):
    n = input("score :")
    num_array.append(float(n))
print ('SCORES: ',num_array)

max_value = max(num_array)
min_value = min(num_array)
avg_value = sum(num_array)/len(num_array)

#print(max_value, min_value, avg_value)
print("max=", max_value)
print("min=", min_value)
print("average=", avg_value)


cont = input("do you wish to continue? y/n:")
if cont == "y":
    print ("continuing...")
if cont == "n":
    quit()
    #sys.exit("OK - all done")

##

limit = float(input("enter score limit for exams:"))
while limit < max_value:
    limit = float(input("limit cannot be smaller than max score, re-enter:"))
#this checks what the exams are scored out of (eg. /100)


def check_is (num, to_check):
    if (num < to_check):
        return True
    else:
        return False


new_num = float(input("enter most recent score:"))
while limit < new_num:
    new_num = float(input("score cannot exceed limit, re-enter:"))

og_num = float(input("enter a score to compare with:"))
while limit < og_num:
    og_num = float(input("score cannot exceed limit, re-enter:"))

##

print ("comparing =", og_num, "|", new_num)

print ("checking if there was an improvement...")
check_score = check_is (og_num, new_num)

if check_score:
    print ("there was an improvement, well done")
    print (og_num, "<", new_num)
else:
    print ("unfortunately no improvement")
    print (og_num, ">", new_num)
        
##    

if min_value <= new_num and new_num <= limit:
    print ("score is within range, you are on track")
    #pass
else:
    print ("score is not within range, maybe you had bad day?")

##

cont = input("do you wish to continue? y/n:")
if cont == "y":
    print ("continuing...")
if cont == "n":
    quit()

old_avg = avg_value

num_array.append(og_num)
num_array.append(new_num)

print ('UPDATED SCORE SET: ',num_array)

max_value = max(num_array)
min_value = min(num_array)
avg_value = sum(num_array)/len(num_array)

#print("max=", max_value)
#print("min=", min_value)
#print("average=", avg_value)

###

print("old average=", old_avg, "| new average=", avg_value)

check_avg = check_is (og_num, new_num)

if check_avg:
    print ("your average has improved, congratulations")
    print (old_avg, "<", avg_value)
else:
    print ("average has declined")
    print (old_avg, ">", avg_value)
        