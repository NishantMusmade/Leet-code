# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


# def isIsomorphic(s, t):
#     letter_mapping = {}
#     for i in range(len(s)):
#         if t[i] in letter_mapping.values() and letter_mapping[s[i]]!=t[i]:
#             return False
#         letter_mapping[s[i]] = t[i]


#     if len(letter_mapping) != len(set(s)):
#         return False
#     test_str = ''
#     for i in range(len(s)):
#         test_str =test_str + letter_mapping[s[i]]
    
#     if test_str == t:
#         return True
#     else:
#         return False
    
# s = 'badc'
# t= 'baba'

# print(isIsomorphic(s,t))


#OR - another approach


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}

    for char_s,char_t in zip(s,t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True
                
    
s = 'badc'
t= 'baba'

print(isIsomorphic(s,t))