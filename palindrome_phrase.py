# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# def remove_non_alphanum(s):
#     return ''.join(char for char in s if char.isalnum())

# def valid_palindrome(s):
#     trimmed_str=remove_non_alphanum(s.lower())
#     print(trimmed_str)

#     i= 0
#     j = len(trimmed_str)-1
#     flag = 1
#     while i < len(trimmed_str)//2:
#         if trimmed_str[i] != trimmed_str[j]:
#             return False
#         i = i+1
#         j = j-1
    
#     return True

# input_string='A man, a plan, a canal: Panama'
# result = valid_palindrome(input_string)
# print(result)


# Another approach


def valid_palindrome(s):
    i = 0   #starting index
    j = len(s) - 1   #end index
    while i<j:
        if s[i].isalnum() == False:
            i = i+1
        elif s[j].isalnum() == False:
            j = j-1
        elif s[i].lower() == s[j].lower():
            i = i+1
            j = j-1
        else:
            return False

    return True 

input_string='race a car'
result = valid_palindrome(input_string)
print(result)
