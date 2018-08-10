## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    if type(word) != str:
        raise TypeError, "You shall not pass."
    else:
        mylist = list(word)
        vowels = ['a', 'e', 'i', 'o', 'u']
        myvowels =[]
        for x in mylist:
            if x in vowels:
                myvowels.append(x)
        return len(myvowels)


