__author__ = 'bhiwalakhil'

# Reads integers as input from stdin, returns product of list of integers, product of those integers, and number of zeros in the list.
def readInput():
    list_input = []
    product = 1
    zero_flag = 0

    try:
        total_words = int(float(raw_input()))
    except:
        print 'Oops! Is your first line a valid number?\nCurrently, I only understand integers. :('
        print 'exiting'
        exit()

    for i in range(total_words):
        try:
            number = int(float(raw_input()))
        except:
            print 'Error: Not a valid integer! Ignoring this value.'
            continue
        # Updates zero_flag with number of zero in input
        if number == 0:
            zero_flag += 1
            if zero_flag > 1:
                product = 0
        else:
            product *= number

        list_input.append(number)
    return (list_input, product, zero_flag)


if __name__ == '__main__':
    list_input, product, zero_flag = readInput()

    # If there are more than 1 zero in input, just print all as zero.
    if zero_flag > 1:
        for _ in range(len(list_input)):
            print 0
    # If there is exactly 1 zero in input, print all as zero except for the element which is zero
    elif zero_flag == 1:
        for elem in list_input:
            if elem is not 0:
                print 0
            else:
                print product
    # Print product divided by that element.
    else:
        for elem in list_input:
            print product / elem