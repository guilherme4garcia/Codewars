#Find the stray number

#You are given an odd-length array of integers, in which all of them are the same, except for one single number.
#Complete the method which accepts such an array, and returns that single different number.


def stray(arr):
    unico = 0
    for number in arr:
        contador = arr.count(number)
        if contador == 1:
            unico = number
    
    return unico
    