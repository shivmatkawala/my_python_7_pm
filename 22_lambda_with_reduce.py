# Lambda with Reduce:

    # Collection ==> Single value output.
    # [1, 2, 3, 4, 5] ==> 15

from functools import reduce

nums = [1, 2, 3, 4, 34, 5, 6, 7, 8, 9]
# total = reduce(lambda num1, num2: num1+num2, nums)
# print(total)

# product = reduce(lambda n1, n2: n1*n2, nums)
# print(product)

# total_count = reduce(lambda total, num: total+1 if num else total, nums, 0)
# print(total_count)

# total_even_nums = reduce(lambda total, num: total+1 if num%2 == 0 else total, nums, 0)
# print(total_even_nums)

# str1 = "APPLEij90#$%U"
# Count the numbe of vowels avialble
# total_vowels = reduce(lambda total, char: total+1 if char.lower() in "aeiou" else total, str1, 0)
# print(total_vowels)

# max_from_nums = reduce(lambda high, num: high if num < high else num, nums, 0)
# print(max_from_nums)

