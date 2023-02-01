# two types of loops are while and for

# while loop
# x=0
# while (x<4):
#     print(x)
#     x=x+1

# # for loop
# for x in range(5,10):
#     print(x)

# arrays
days=["sunday", "monday", "tuesday", "wednes", "thursday", "saturday"]
for j in days:
    #if j=="thursday": break # loop stops at thursday
    if j=="thursday": continue # skips thursday
    print(j)