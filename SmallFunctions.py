# sum of digits
def DigitSum(n):
    result = 0
    while (n>0):
        remain = n%10
        result += remain
        n /= 10
    return result


print DigitSum(1234)


# Factotial of a number
def factorial(x):
    if (x==1): return 1
    return x*factorial(x-1)

print factorial(4)


# Check if the number is prime
def is_prime(x):
    if x == 0 or x == 1 or x < 0: return False
    for n in range(2,x):
        if (x%n == 0): return False
    return True

# Reverse a string (simple solution)
def reverse(text):
    indexOfText = len(text)- 1
    reversedText = ""
    while indexOfText >= 0:
        reversedText += text[indexOfText]
        indexOfText -= 1
    return reversedText

print reverse("Hello")

#anti_vowel
def anti_vowel(text):
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U" :
            text = text.replace(char,"")
    return text

print anti_vowel("Hey You!")

#Scrabble_score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                "x": 8, "z": 10}

def scrabble_score(word):
    result = 0
    word = word.lower()
    for char in word:
        result += score[char]
    return result

print scrabble_score("Helix")

# Count number in a sequence
def count(sequence,item):
    count = 0
    for number in sequence:
        if number == item:
            count+=1
    return count

print count([1,2,1,1],1)

# Purify, filter the odd numbers
def purify(numbers):
    result = []
    for number in numbers:
        if (number%2 == 0):
            result.append(number)
    return result

print purify([4,5,5,4])

# remove duplicates
def remove_duplicates(numbers):
    new_numbers = []
    for number in numbers:
        if (number not in new_numbers):
            new_numbers.append(number)
    return new_numbers


print remove_duplicates([1,1,2,2])

# Find median in a list of numbers
def median(numbers):
    result = 0
    numbers = sorted(numbers)
    n = len(numbers)
    if (n%2==1):
        result = numbers[int(n/2)]
    else:
        result = (numbers[n/2]+numbers[n/2 - 1])/2.0
    return result

print median([4,5,5,4])

#Censor
def censor(text,word):
    text = text.split(" ")
    for index in range(len(text)):
        if (text[index] == word):
            text[index] = "*" * len(word)
    return " ".join(text)


print censor("hey hey hey","hey")

# Computing the average
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    result = 0
    for score in scores:
        result += score
    return result

def grades_average(grades):
    return grades_sum(grades)/float(len(grades))

print grades_sum(grades)
print grades_average(grades)
