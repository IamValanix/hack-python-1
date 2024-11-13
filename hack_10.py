"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    output = []

    for i in result[0:]:
        if i == 'O':
            output.append('0')
        elif i == 'I':
            output.append('1')
        elif i == 'A':
            output.append('@')
        else:
            output.append(i)
    print(output)
    return result  
fn_hack_10()