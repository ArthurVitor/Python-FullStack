#Write a function that receives 2 numbers, the first one is a value and the second one it's a percentage
#Return the first parameter + his own percentage (Value 2)

def percentage(value, per):
    return f'{value + (value * (per/100))}'

print(percentage(1000, 10))