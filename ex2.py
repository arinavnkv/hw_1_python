string = input("Введите строку: ")

def is_palindrome(s):
    string = s[::-1]
    if s == string:
        return True
    else:
        return False

if is_palindrome(string):
    print("Это палиндром")
else:
    print("Это не палиндром")