def convert_to_decimal(a,b):
        i = len(a)-1
        j=0
        sum = 0 

        while i>=0:
            sum += int(a[i])* 2**j
            i=i-1
            j=j+1
        
        a_dec = sum
        
        i = len(b)-1
        j=0
        sum = 0
        while i>=0:
            sum+= int(b[i])* 2**j
            i=i-1
            j=j+1
        
        b_dec = sum

        return a_dec,b_dec


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a_dec,b_dec = convert_to_decimal(a,b)

    output_str_dec = a_dec + b_dec
    output_str_bin = ''
    while output_str_dec > 0:
        remainder = output_str_dec % 2
        output_str_bin = str(remainder) + str(output_str_bin)
        output_str_dec = output_str_dec//2
    if output_str_bin=='':
        return '0'
    return output_str_bin

a = '1010'
b = '1011'

print('Addition of binary string is: ',addBinary(a,b))