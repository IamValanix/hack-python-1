"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    x = 1
    while x <= 5:
        result.insert(x,'@')
        x += 2
    print(result)
    return result   
fn_hack_9()