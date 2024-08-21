
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    regular_roman ={
        'I': 1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    exception_roman = {
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900,
    }
    number = {}
    len_s = len(s)
    j=0
    while j<len_s:
        if j!=len_s-1:
            letter = s[j]+s[j+1]
            print(letter)
            if letter in exception_roman:
                j=j+2
                print(j)
                if letter in number:
                    number[letter]=number[letter]+exception_roman[letter]
                else:
                    number[letter]= exception_roman[letter]
                print(number)
            else:
                letter = s[j]
                print(letter)
                if letter in number:
                    number[letter]=number[letter]+regular_roman[letter]
                else:
                    number[letter]=regular_roman[letter]
                j=j+1
                print(j)
                print(number)
        else:
            letter = s[j]
            if letter in number:
                number[letter]=number[letter]+regular_roman[letter]
            else:
                number[letter]=regular_roman[letter]
            j=j+1
    
    print(number)

    sum =0
    for key,value in number.items():
        sum += value
    print(sum)

romanToInt('III')
        

            

