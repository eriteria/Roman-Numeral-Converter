from RomanNumeralsReverse import NumberToRoman

y = input()
z = 0
if y.isnumeric():
    print(f"{y} in Roman Numerals is {NumberToRoman(y)}")
if not (y.isnumeric()):
    while y != z:
        for i in range(1, 4000):
            z = NumberToRoman(i)
            if y == z:
                print(f"{y} in Figures is {i}")
        else:
            break


