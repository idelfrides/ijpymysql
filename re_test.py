

import re


def test_re():
    my_value = 'obama teste 1125'

    res = re.match(r"\w+", my_value)

    if res:
        print('\n\n MATCH \n\n RESULT -> ',res.string)

    if not res:
        print('\n\n NOT MATCH \n\n RESULT:  ', 
            res.string       
        )

    print('\n\n\n\n\n')

if __name__=='__main__':
    test_re()
