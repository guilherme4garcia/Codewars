# Find the unique number

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    
    for number in arr:
        if arr.count(number) == 1:
            unique = number

    return unique