def NumberToRoman(x):
    x = str(x)
    l = len(x)
    y = []
    f = ''

    for i,j in enumerate(x):
        j = int(j)
        a = j*10**(l-i-1)
        y.append(a)

    if len(y) == 4:
        f = 'M' * (y[0] // 1000)
        if y[1] == 500:
            f = f + 'D'
        elif y[1] == 900:
            f = f + 'CM'
        elif (y[1] > 500) and (y[1] < 900):
            q = y[1] - 500
            w = (q // 100) * 'C'
            f = f + 'D' + w
        elif (y[1] < 500) and (y[1] > 300):
            e = 500 - y[1]
            r = (e // 100) * 'C'
            f = f + r + 'D'
        elif y[1] == 100:
            f = f + 'C'
        elif (y[1] == 200) or (y[1] == 300):
            h = y[1]//100
            f = f + ('C' * h)
        if y[2] == 10:
            f = f + 'X'
        elif y[2] == 50:
            f = f + 'L'
        elif y[2] == 90:
            f = f + 'XC'
        elif y[2] > 50 and y[2] < 90:
            q = y[2] - 50
            w = (q // 10) * 'X'
            f = f + 'L' + w
        elif y[2] < 50 and y[2] > 30:
            e = 50 - y[2]
            r = (e // 10) * 'X'
            f = f + r + 'L'
        elif (y[2] == 20) or (y[2] == 30):
            h = y[2]//10
            f = f + ('X' * h)
        if y[3] == 1:
            f = f + 'I'
        elif y[3] == 5:
            f = f + 'V'
        elif y[3] == 9:
            f = f + 'IX'
        elif y[3] > 5 and y[3] < 9:
            q = y[3] - 5
            w = q * 'I'
            f = f + 'V' + w
        elif y[3] < 5 and y[3] > 3:
            e = 5 - y[3]
            r = e * 'I'
            f = f + r + 'V'
        elif (y[3] == 2) or (y[3] == 3):
            h = y[3]
            f = f + ('I' * h)  

    if len(y) == 3:
        if y[0] == 500:
            f = f + 'D'
        elif y[0] == 900:
            f = f + 'CM'
        elif (y[0] > 500) and (y[0] < 900):
            q = y[0] - 500
            w = (q // 100) * 'C'
            f = f + 'D' + w
        elif (y[0] < 500) and (y[0] > 300):
            e = 500 - y[0]
            r = (e // 100) * 'C'
            f = f + r + 'D'
        elif y[0] == 100:
            f = f + 'C'
        elif (y[0] == 200) or (y[0] == 300):
            h = y[0]//100
            f = f + ('C' * h)
        if y[1] == 10:
            f = f + 'X'
        elif y[1] == 50:
            f = f + 'L'
        elif y[1] == 90:
            f = f + 'XC'
        elif y[1] > 50 and y[1] < 90:
            q = y[1] - 50
            w = (q // 10) * 'X'
            f = f + 'L' + w
        elif y[1] < 50 and y[1] > 30:
            e = 50 - y[1]
            r = (e // 10) * 'X'
            f = f + r + 'L'
        elif (y[1] == 20) or (y[1] == 30):
            h = y[1]//10
            f = f + ('X' * h)
        if y[2] == 1:
            f = f + 'I'
        elif y[2] == 5:
            f = f + 'V'
        elif y[2] == 9:
            f = f + 'IX'
        elif y[2] > 5 and y[2] < 9:
            q = y[2] - 5
            w = q * 'I'
            f = f + 'V' + w
        elif y[2] < 5 and y[2] > 3:
            e = 5 - y[2]
            r = e * 'I'
            f = f + r + 'V'
        elif (y[2] == 2) or (y[2] == 3):
            h = y[2]
            f = f + ('I' * h)  

    if len(y) == 2:
        if y[0] == 10:
            f = f + 'X'
        elif y[0] == 50:
            f = f + 'L'
        elif y[0] == 90:
            f = f + 'XC'
        elif y[0] > 50 and y[0] < 90:
            q = y[0] - 50
            w = (q // 10) * 'X'
            f = f + 'L' + w
        elif y[0] < 50 and y[0] > 30:
            e = 50 - y[0]
            r = (e // 10) * 'X'
            f = f + r + 'L'
        elif (y[0] == 20) or (y[0] == 30):
            h = y[0]//10
            f = f + ('X' * h)
        if y[1] == 1:
            f = f + 'I'
        elif y[1] == 5:
            f = f + 'V'
        elif y[1] == 9:
            f = f + 'IX'
        elif y[1] > 5 and y[1] < 9:
            q = y[1] - 5
            w = q * 'I'
            f = f + 'V' + w
        elif y[1] < 5 and y[1] > 3:
            e = 5 - y[1]
            r = e * 'I'
            f = f + r + 'V'
        elif (y[1] == 2) or (y[1] == 3):
            h = y[1]
            f = f + ('I' * h)  

    if len(y) == 1:
        if y[0] == 1:
            f = f + 'I'
        elif y[0] == 5:
            f = f + 'V'
        elif y[0] == 9:
            f = f + 'IX'
        elif y[0] > 5 and y[0] < 9:
            q = y[0] - 5
            w = q * 'I'
            f = f + 'V' + w
        elif y[0] < 5 and y[0] > 3:
            e = 5 - y[0]
            r = e * 'I'
            f = f + r + 'V' 
        elif (y[0] == 2) or (y[0] == 3):
            h = y[0]
            f = f + ('I' * h)  
                
    return f
def main():
    print(NumberToRoman(123))

if __name__ == "__main__":
    main()