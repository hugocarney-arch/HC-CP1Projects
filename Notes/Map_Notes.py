# HC Maps Notes
def times(number):
    return number *2

numbers = range(1, 6)

multiplied_numbers = map(times,numbers)

print(*list(multiplied_numbers))
