"""Does word contain more vowels than non-vowels?

If the word is over half vowels, it should return True:

    >>> has_more_vowels("moose")
    True

If it's half vowels (or less), it's false:

    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

Don't consider "y" as a vowel:

    >>> has_more_vowels("yay")
    False

Uppercase vowels are still vowels:

    >>> has_more_vowels("Aal")
    True
"""


def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""
    vowels = 'aeiou'

    count_vowels = 0
    count_not_vowels = 0
    for char in word.lower():
        if char in vowels:
            count_vowels+= 1
        else:
            count_not_vowels+= 1

    if count_vowels > count_not_vowels:
        return True   
    return False        




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
