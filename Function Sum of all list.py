#Function Sum of all list
#solution 1
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total  # return should be outside the loop
print(sum([2, 4, 6, 8, 10])) 