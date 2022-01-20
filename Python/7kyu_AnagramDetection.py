#Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

def is_anagram(test, original):
    test_sort = sorted(test.lower())
    original_sort = sorted(original.lower())

    if test_sort == original_sort:
        return True
    else:
        return False