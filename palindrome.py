def ispalindrome(num):
    reverse_num = []
    digit_count = 0
    while num>0:
        remainder = num%10
        num = num//10
        reverse_num.append(remainder)
        digit_count+=1
    
    sum = 0
    for num in reverse_num:
        smallest_digit = 10**(digit_count-1)
        num = num * smallest_digit
        sum += num
        digit_count-=1

    return sum
    
    
num = int(input('Enter a number: '))
result= ispalindrome(num)

if num==result:
    print('\nThe given number is palindrome')
else:
    print('\nThe given number is not palindrome')

