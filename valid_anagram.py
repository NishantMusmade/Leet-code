# def isAnagram(s, t):
#     if len(s)!=len(t):
#         return False
#     else:
#         dict_s = {s[0]: 0}
#         # dict_t = {t[0]:0}

#         for char_s,char_t in zip(s,t):
#             if char_s not in dict_s:
#                 dict_s[char_s] = 1
#             else:
#                 dict_s[char_s] += 1
#             if char_t not in dict_s:
#                 dict_s[char_t] = -1
#             else:
#                 dict_s[char_t] -=1
                  
#     print(dict_s)
#     for value in dict_s.values():
#         if value != 0:
#             return False
    
#     return True
    

    # OR


def isAnagram(s,t):
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    for c in count:
        if c!=0:
            return False
    
    return True



s = 'anagram'
t = 'nagaram'

print(isAnagram(s,t))
