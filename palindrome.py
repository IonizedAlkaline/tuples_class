def palindrome(t):
    ending = len(t) - 1
    starting = 0
    while starting < ending:
        if t[starting] != t[ending]:
            return False
        starting = starting + 1
        ending = ending - 1
    return True


tuples = (1, 2, 3, 1)
if palindrome(tuples) == True:
    print("its a palindrome ")
else:
    print("its not a palindrome")
