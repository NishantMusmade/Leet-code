exception_roman = {
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900,
    }
num={}
letter = 'IV'
if letter in exception_roman:
    num[letter] = exception_roman[letter]*2
    print(num)