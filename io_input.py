def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

text = input("Enter something: ")

if is_palindrome(text):
    print("its a palindrome")
else:
    print("its not a palindrome")

