# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"



#Following code implementation is using stack

# def reverseVowels(s):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     stack = []
    
#     for i in s:
#         if i in vowels:
#             stack.append(i)
    
#     reverse_vowels = ''
#     for i in s:
#         if i in vowels:
#             reverse_vowels = reverse_vowels + stack.pop()
#         else:
#             reverse_vowels = reverse_vowels + i
    
#     return reverse_vowels

# OR

#Two pointer approach

def reverseVowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    output = list(s)

    l = 0
    r = len(s) - 1

    while l<r:
        while l<r and output[l] not in vowels:
            l+=1
        while l<r and output[r] not in vowels:
            r-=1
        temp = output[l]
        output[l] = output[r]
        output[r] = temp

        l+=1
        r-=1
 
    return ''.join(output)


s = 'IceCream'
print(reverseVowels(s))