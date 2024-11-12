"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    x = 5
    while x >= 0:
        result.append(x)
        x -= 1
    print (result)
    return result  

fn_hack_7()