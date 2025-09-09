word = input("")

palindrome = word[::-1]

if word.lower() == palindrome.lower():
    print("Palindrome!")
else:
    print("Nothing special about this string :(")