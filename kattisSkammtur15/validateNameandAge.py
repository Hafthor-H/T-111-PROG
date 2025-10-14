def contains_letters_and_spaces(s: str):
    return any(ch.isalpha() for ch in s) and all(ch.isalpha() or ch.isspace() for ch in s)
#                   ^                                         ^
#                   |                                         |___ Þetta loop sér til þess að það séu bara stafir eða bil
#                   |
#                   |____Þetta loop passar upp á það sé amk einn stafur
def get_name():
    while True:
        print("What's your name?")
        name = input()
        if contains_letters_and_spaces(name):
            return name
        print("Please enter a valid name.")

def get_age():
    while True:
        print("How old are you?")
        try:
            age = input()
            if int(age) < 0 or int(age) > 125:
                print(f"You seriously expect me to believe you are {age} years old?")
                continue
            else:
                return age
        except:
            print("Please enter an integer.")

name = get_name()
age = get_age()

print(f"Nice to meet you {name}. Congratulations on your {age} years.")




























# def get_name():
#     print("What's your name?")
#     name = input()
#     if name == " ":
#         get_name()
#     elif contains_letters_and_spaces(name):
#         return name
#     else:
#         print("Please enter a valid name.")
#         get_name()

# def get_age():
#     print("How old are you?")
#     try:
#         age = int(input())
#         if age < 0 or age > 125:
#             print(f"You seriously expect me to believe you are {age} years old?")
#             get_age()
#         else:
#             return age
#     except:
#         print("Please enter an integer.")
#         get_age()