name =[]
x: int = 1
while(x == 1):
    y1 = int(input('1 for numbers, 2 for letters: '))
    if (y1 == 2):
        x1 = str(input('type your letter: '))
        code: str = ' '
        if (x1 == 'a' or x1 == 'A'):
            code = '.-'
        elif (x1 == 'b' or x1 == 'B'):
            code =  '-...'
        elif (x1 == 'c' or x1 == 'C'):
            code = '-.-.'
        elif (x1 == 'd' or x1 == 'D'):
            code = '-..'
        elif (x1 == 'e' or x1 == 'E'):
            code = '.'
        elif (x1 == 'f' or x1 == 'F'):
            code = '..-.'
        elif (x1 == 'g' or x1 == 'G'):
            code = '--.'
        elif (x1 == 'h' or x1 == 'H'):
            code = '....'
        elif (x1 == 'i' or x1 == 'I'):
            code = '..'
        elif (x1 == 'j' or x1 == 'J'):
            code = '.---'
        elif (x1 == 'k' or x1 == 'K'):
            code = '-.-'
        elif (x1 == 'l' or x1 == 'L'):
            code = '.-..'
        elif (x1 == 'm' or x1 == 'M'):
            code = '--'
        elif (x1 == 'n' or x1 == 'N'):
            code = '-.'
        elif (x1 == 'o' or x1 == 'O'):
            code = '---'
        elif (x1 == 'p' or x1 == 'P'):
            code = '.--.'
        elif (x1 == 'q' or x1 == 'Q'):
            code = '--.-'
        elif (x1 == 'r' or x1 == 'R'):
            code = '.-.'
        elif (x1 == 's' or x1 == 'S'):
            code = '...'
        elif (x1 == 't' or x1 == 'T'):
            code = '-'
        elif (x1 == 'u' or x1 == 'U'):
            code = '..-'
        elif (x1 == 'v' or x1 == 'V'):
            code = '...-'
        elif (x1 == 'w' or x1 == 'W'):
            code = '.--'
        elif (x1 == 'x' or x1 == 'X'):
            code = '-..-'
        elif (x1 == 'y' or x1 == 'Y'):
            code = '-.--'
        elif (x1 == 'z' or x1 == 'Z'):
            code = '--..'
        elif (x1 == ' ' or x1 == ' '):
            code = ' '
        print('letter:', x1, 'is:', code)
        y = code
        name.append(y)
        print(name)
    elif(y1 == 1):
        x2 = int(input('type your number: '))
        code1: int = 0
        if (x2 == 0):
            code1 = '-----'
        elif (x2 == 1):
            code1 =  '.----'
        elif (x2 == 2):
            code1 = '..---'
        elif (x2 == 3):
            code1 = '...--'
        elif (x2 == 4):
            code1 = '....-'
        elif (x2 == 5):
            code1 = '.....'
        elif (x2 == 6):
            code1 = '-....'
        elif (x2 == 7):
            code1 = '--...'
        elif (x2 == 8):
            code1 = '---..'
        elif (x2 == 9):
            code1 = '----.'
        elif (x2 == ' '):
            code = ' '
        print('the number: ', x2, 'is: ', code1)
        y = code1
        name.append(y)
        print(name)
    x = int(input('type 1 for continue'))
