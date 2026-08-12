def add_two_numbers() -> int:
    line = input()
    nums = line.split(",")
    count = 0 
    for n in nums:
        count+=int(n)
    return count


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
