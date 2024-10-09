# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

def titleToNumber(columnTitle):   
    sum  = 0
    i = len(columnTitle)-1
    j = 0
    while i >=0:
        current_letter_value = (ord(columnTitle[i])-64) * 26**j    
        sum = sum + current_letter_value
        i = i-1
        j= j+1
    
    return sum

columnTitle = 'AB'
print(titleToNumber(columnTitle))



# ord(columnTitle[i])-64 
# Example : Title = A then ord(A) = 65 and 65-64 = 1, position of A in alphabet
#                   B then ord(B) = 66 and 66-64 = 2, position of B in Alphabet