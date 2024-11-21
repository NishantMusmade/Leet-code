# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s):
        i = 0
        j = len(s)-1

        while i<=(len(s)-1)//2:
            temp = s[i]
            s[i]=s[j]
            s[j] = temp
            i+=1
            j-=1
        
        return s

s = ["h","e","l","l","o"]
print(reverseString(s))