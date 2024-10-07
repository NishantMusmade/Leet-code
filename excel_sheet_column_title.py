# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

def convertToTitle(columnNumber):
    columnTitle = ''
    while columnNumber>=1:
        columnNumber-=1
        remainder = columnNumber%26
        columnTitle = chr(65+remainder) + columnTitle 
        columnNumber = columnNumber//26

    return columnTitle 

columnNumber = 701
print(convertToTitle(columnNumber)) 

