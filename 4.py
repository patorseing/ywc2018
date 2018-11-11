def cardAt(pos):
    suitcard = ['C', 'D', 'H', 'S']
    try:
        suit = int(pos/13)
        num = pos % 13
        if num == 12:
            num = 'A'
        elif num == 11:
            num = 'K'
        elif num == 10:
            num = 'Q'
        elif num == 9:
            num = 'J'
        else:
            num = (num + 2) % 10
        return str(num)+suitcard[suit]
    except:
        return 'error'


n = input('Enter card position: ')
try:
    print("cardAt({})".format(n), "=", cardAt(int(n)))
except:
    print('error')


"""
for x in range(0, 52):
    print('pos', int(x), ': ', cardAt(int(x)))
"""
