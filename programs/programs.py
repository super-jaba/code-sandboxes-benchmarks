# String operations
program_1 = '''
result = "Hello" + " " + "World"
print(result)
'''
expected_1 = "Hello World"

program_2 = '''
text = "Python Programming"
result = text[0:6]
print(result)
'''
expected_2 = "Python"

program_3 = '''
text = "hello world"
result = text.upper()
print(result)
'''
expected_3 = "HELLO WORLD"

program_4 = '''
text = "PYTHON"
result = text.lower()
print(result)
'''
expected_4 = "python"

program_5 = '''
text = "  spaced  "
result = text.strip()
print(result)
'''
expected_5 = "spaced"

program_6 = '''
text = "apple,banana,cherry"
result = text.split(",")
print(result)
'''
expected_6 = "['apple', 'banana', 'cherry']"

program_7 = '''
text = "hello"
result = text.replace("l", "L")
print(result)
'''
expected_7 = "heLLo"

program_8 = '''
name = "Alice"
age = 25
result = f"{name} is {age} years old"
print(result)
'''
expected_8 = "Alice is 25 years old"

program_9 = '''
text = "programming"
result = len(text)
print(result)
'''
expected_9 = "11"

program_10 = '''
text = "Hello"
result = text * 3
print(result)
'''
expected_10 = "HelloHelloHello"

# Math operations
program_11 = '''
a = 10
b = 5
result = a + b
print(result)
'''
expected_11 = "15"

program_12 = '''
a = 20
b = 7
result = a - b
print(result)
'''
expected_12 = "13"

program_13 = '''
a = 6
b = 7
result = a * b
print(result)
'''
expected_13 = "42"

program_14 = '''
a = 15
b = 3
result = a / b
print(result)
'''
expected_14 = "5.0"

program_15 = '''
a = 17
b = 5
result = a // b
print(result)
'''
expected_15 = "3"

program_16 = '''
a = 17
b = 5
result = a % b
print(result)
'''
expected_16 = "2"

program_17 = '''
a = 2
b = 8
result = a ** b
print(result)
'''
expected_17 = "256"

program_18 = '''
x = 10
y = 20
result = max(x, y)
print(result)
'''
expected_18 = "20"

program_19 = '''
x = 10
y = 20
result = min(x, y)
print(result)
'''
expected_19 = "10"

program_20 = '''
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)
'''
expected_20 = "15"

program_21 = '''
x = 25
result = x ** 0.5
print(result)
'''
expected_21 = "5.0"

program_22 = '''
x = 3.7
result = round(x)
print(result)
'''
expected_22 = "4"

program_23 = '''
x = -10
result = abs(x)
print(result)
'''
expected_23 = "10"

program_24 = '''
a = 5
b = 10
c = 15
result = (a + b) * c
print(result)
'''
expected_24 = "225"

# Array/List operations
program_25 = '''
arr = [1, 2, 3]
arr.append(4)
print(arr)
'''
expected_25 = "[1, 2, 3, 4]"

program_26 = '''
arr = [1, 2, 3, 4, 5]
result = arr[1:4]
print(result)
'''
expected_26 = "[2, 3, 4]"

program_27 = '''
arr = [3, 1, 4, 1, 5]
result = sorted(arr)
print(result)
'''
expected_27 = "[1, 1, 3, 4, 5]"

program_28 = '''
arr = [1, 2, 3, 4, 5]
result = len(arr)
print(result)
'''
expected_28 = "5"

program_29 = '''
arr = [1, 2, 3]
result = arr * 2
print(result)
'''
expected_29 = "[1, 2, 3, 1, 2, 3]"

program_30 = '''
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = arr1 + arr2
print(result)
'''
expected_30 = "[1, 2, 3, 4, 5, 6]"

program_31 = '''
arr = [1, 2, 3, 4, 5]
result = arr[::-1]
print(result)
'''
expected_31 = "[5, 4, 3, 2, 1]"

program_32 = '''
arr = [1, 2, 3, 4, 5]
result = arr[0]
print(result)
'''
expected_32 = "1"

program_33 = '''
arr = [1, 2, 3, 4, 5]
result = arr[-1]
print(result)
'''
expected_33 = "5"

program_34 = '''
arr = [5, 2, 8, 1, 9]
result = max(arr)
print(result)
'''
expected_34 = "9"

program_35 = '''
arr = [5, 2, 8, 1, 9]
result = min(arr)
print(result)
'''
expected_35 = "1"

program_36 = '''
arr = [1, 2, 3]
arr.insert(1, 99)
print(arr)
'''
expected_36 = "[1, 99, 2, 3]"

program_37 = '''
arr = [1, 2, 3, 2, 4]
result = arr.count(2)
print(result)
'''
expected_37 = "2"

program_38 = '''
arr = [1, 2, 3, 4, 5]
result = [x * 2 for x in arr]
print(result)
'''
expected_38 = "[2, 4, 6, 8, 10]"

program_39 = '''
arr = [1, 2, 3, 4, 5, 6]
result = [x for x in arr if x % 2 == 0]
print(result)
'''
expected_39 = "[2, 4, 6]"

program_40 = '''
arr = [1, 2, 3]
arr.pop()
print(arr)
'''
expected_40 = "[1, 2]"

program_41 = '''
arr = [1, 2, 3]
arr.remove(2)
print(arr)
'''
expected_41 = "[1, 3]"

program_42 = '''
arr = [3, 1, 4, 1, 5]
arr.sort()
print(arr)
'''
expected_42 = "[1, 1, 3, 4, 5]"

program_43 = '''
arr = [1, 2, 3]
result = sum(arr)
print(result)
'''
expected_43 = "6"

program_44 = '''
arr = [1, 2, 3, 4, 5]
result = arr[::2]
print(result)
'''
expected_44 = "[1, 3, 5]"

program_45 = '''
arr = [1, 2, 3]
result = arr.index(2)
print(result)
'''
expected_45 = "1"

