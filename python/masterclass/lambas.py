nums = [10, 14, 21, 50, 5, -6]

def square(value):
    return value ** 2
# squared_nums = []
# for num in nums:
#     squared_nums.append(num ** 2)

squared_nums = list(map(square, nums))
print(squared_nums)