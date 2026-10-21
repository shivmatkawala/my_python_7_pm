# Lambda with filter():

    # Filter is used on collection to filter out values
    # and get intended output.

# numbers = [2, 3, 8, 9, 0, 5, 6, 11, 13, 23, 78, 45, 67, 90]
# # Get only those numbers which are greater than 50

# greater_than_50_nums = list(filter(lambda num: num if num> 50 else None, numbers))
# print(greater_than_50_nums)


# Write a filter program with lambda to get only those stings
# which are containing consonents

my_strings = ["oeo", "aeo", "keo", "tuo", 'ooe', 'eoe']

strings_with_consonents = list(
    filter(
        lambda string: any(char not in "aeiou" for char in string),
        my_strings
    )
)

print(strings_with_consonents)