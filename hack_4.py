"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1].lower()+result[7].upper()
    #comprobando el resultado
    print (result)
    return result

fn_hack_4()
