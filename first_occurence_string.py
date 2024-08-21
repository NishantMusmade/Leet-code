def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # index = -1
        # len_needle = len(needle)
        # j=0
        # for i in range(len(haystack)-len(needle)+1):
        #     print(haystack)
        #     print(i)
        #     if haystack[i:len(needle)+j] == needle:
        #         index = i
        #         break
        #     j=j+1
        # print(index)
        # def strStr(self, haystack, needle):
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                return i
        # if we exit the loop, return -1        
        return -1
            

haystack = "hg"
needle = "hg"
index = strStr(haystack,needle)
print(index)