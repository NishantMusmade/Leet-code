def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    min = len(strs[0])
    for i in strs:
        if min >= len(i):
            min = len(i)

    min_trimmed_string = []
    for i in strs:
        i = i[:min]
        min_trimmed_string.append(i)
    len_string_list = len(min_trimmed_string)
    if '' not in min_trimmed_string and len_string_list>1:
        i=0
        flag = 0
        common_prefix = ''
        for j in range(len(min_trimmed_string[0])):
            for k in range(len(min_trimmed_string)-1):
                if min_trimmed_string[i][j]!=min_trimmed_string[k+1][j]:
                    flag = 1
                    break
            if flag ==0:
                common_prefix = common_prefix+min_trimmed_string[i][j]
            else:
                break
    else :
        common_prefix = min_trimmed_string[0]
        
    return common_prefix
            

    

strs = ['a','']
longest_common_prefix=longestCommonPrefix(strs)
print(longest_common_prefix)
