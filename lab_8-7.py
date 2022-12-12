# author: JHR 12/12/22

# defining my function
def is_palindrome(word):
    i = 0
    while len(word)>=i:
        if word.lower() == word.lower()[::-1]:
            i+=1
            return True
        else:
            i+=1
            return False

# test cases
print(is_palindrome("tacocat"))
print(is_palindrome("hi"))
print(is_palindrome("racecar"))
print(is_palindrome("auauauauauauauauau"))
print(is_palindrome("BOb"))
print(is_palindrome("what"))