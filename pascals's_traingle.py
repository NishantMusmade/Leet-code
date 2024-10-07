# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

def generate(numRows):
    output = []
    for i in range(0,numRows):
        output.append([0] *(i+1))

    for i in range(numRows):
        for j in range(i+1):
            if j==0 or j == i:
                # print(i,j)
                output[i][j] = 1
            else:
                x = i-1
                y = j-1
                output[i][j] = output[x][y] + output[x][j]

    return output


numRows = 5
triangle = generate(numRows)
print(triangle)