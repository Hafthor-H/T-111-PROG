num1 = input()
num2 = input()

def divide_safe(num1_str, num2_str):
    try:
        result = round(float(num1_str) / float(num2_str), 5)
        return result
    except (ValueError, ZeroDivisionError):
        return None

print(divide_safe(num1,num2))