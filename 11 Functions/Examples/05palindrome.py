def is_palindrome(s):
    s = s.lower().replace(" ","").replace("'","")
    return s == s[::-1]



s = "Was it a car or a cat I saw"
print(is_palindrome(s))
