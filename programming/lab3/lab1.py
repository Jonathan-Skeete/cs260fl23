from icecream import ic

'''
    Convert the code from lab-1 into a function definition.
    function header is provided to indicate input parameters and output data type

    
    replace pass keyword in the function body with code from lab-1.
'''

def weighted_sum(num: str, base = 10) -> int:
    ''' returns decimal integer representation of num '''
    # pass
    #sample code from lab-1 if you need it.

    lookup_table = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }

    # num = input("please enter a number number: ")
    # base = int(input("please enter a base: "))

    index = 0
    try:
        index_of_point = num.index('.')
        exponent = index_of_point - 1
    except:
        exponent = len(num) - 1
        index_of_point = None


    result_value = 0 # accumulator
    ic(exponent)
    while index <= len(num) - 1:
        if index == index_of_point:
            index +=1
            continue
        result_value += lookup_table[num[index]] * base**exponent
        index += 1
        exponent -= 1

    return result_value

if __name__ == '__main__':
    # num = '01100010'
    # num = '1101.101'
    num = '1a3.4b' # expected 419.29296875
    # num = '101.1010'

    ic( weighted_sum(num, base = 16))
