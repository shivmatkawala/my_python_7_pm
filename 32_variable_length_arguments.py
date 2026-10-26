# Variable Length Arguments:

    # Write a function to perform addition of numbe
def addition(*nums):
    total = 0
    for num in nums:
        total+=num
    print(total)



# addition(2, 3)
# addition(5, 6, 7)
# addition(1, 2, 3,4, 5, 6, 7, 8, 9, 23, 456)


# write a function to get the numbers which are less than 20 

def nums_less_than_20(*nums):
    for num in nums:
        if num < 20:
            print(num)

# nums_less_than_20(89, 23, 45, 1, 8, -56, 0, -34)


# Write a function to get the alphabets whicha are lowercase from bellow
# charecters.

def get_alpha(*chars):
    for char in chars:
        if char.isalpha():
            print(char)

# get_alpha("S", "8", "0", "%", "y", "g", "Z", "@")
