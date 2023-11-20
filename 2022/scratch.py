'''
I want something to take a list of decimal values and turn it into an ascii string,
so [120, 121, 122] would return "xyz"
also from a character form of integers so ['120','121','122'] would also return 'xyz'
limited to 0-9,A-Z,a-z, so ascii 48-122 (inclusive)
'''

def make_string_num(mylist):
    '''
    expecting a list of decimal numbers between 48 and 122
    '''
    mystring = ''
    for item in mylist:
        if (item > 47) and (item < 123):
            mystring = mystring + chr(item)
        else:
            return(False)
    return(mystring)

def make_string_char_num(mylist):
    '''
    expecting a list of strings that are decimal numbers between 48 and 122
    '''
    mystring = ''
    for item in mylist:
        try:
            itemnum = int(item)
        except:
            return(False)
        if (itemnum > 47) and (itemnum < 123):
            mystring = mystring + chr(itemnum)
        else:
            return(False)
    return(mystring)

def make_string_digits(mystring):
    '''
    take a string and turn it into a list of ascii numbers so
    'xyz' becomes [120,121,122]
    '''
    mylist = []
    for x in mystring:
        mylist.append(ord(x))
    return(mylist)

