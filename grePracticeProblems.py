#GRE Quant Practice Problems - https://www.youtube.com/watch?v=ZvdXkDUaavc

#------------------------------------------------------------------------------


#QUESTION -> How many positive integers less than 200 are divisible by 4 or 5?

#two lines of code answer
blab = lambda x: x%4==0 or x%5==0
arrayOfFourOrFive = [item for item in range(1,200) if blab(item)]
print (len(arrayOfFourOrFive))

#one line of code answer 
blah = filter(lambda x: x%4==0 or x%5==0, range(1,200))
print(len(list(blah))) 

#------------------------------------------------------------------------------


#QUESTION -> If x is an integer less than 10, how many different triangles are possible?
#
#                  ,
#                 / \
#                /   \
#               /     \
#          x   /       \   x-2
#             /         \
#            /           \
#           /             \
#           ```````````````
#                  5
#
#
