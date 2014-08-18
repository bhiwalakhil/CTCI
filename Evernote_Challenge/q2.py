__author__ = 'bhiwalakhil'

# Returns k most frequent words in a list sorted by their occurence. In case of tie, sorts in lexicographical order.
def most_frequent_words(input_list, k):
    word_dict = {}
    for word in input_list:
        word = word.strip()
        word_dict[word] = word_dict.get(word, 0) + 1

    sorted_word_list = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

    return [x[0] for x in sorted_word_list][:k]


# Reads input from stdin with 1st line as count of number of upcoming lines. Last line contains k.
def readInput():
    list_input = []
    try:
        total_words = int(raw_input())
    except:
        print 'Oops! Is your first line a valid number?\nCurrently, I only understand integers. :('
        print 'exiting'
        exit()
    list_input.append(total_words)
    for i in range(total_words + 1):
        list_input.append(raw_input())
    return list_input

    # To read input from a file
    # with open('input.txt', 'r') as fp:
    # list_input = fp.readlines()
    # return list_input


if __name__ == '__main__':
    list_input = readInput()
    total_words = list_input[0]
    try:
        k = int(list_input[-1])
    except:
        print 'Error: k must be an integer'

    # if k > total number of words in list, then assign k as all the numbers and return the list.
    if k > total_words:
        k = total_words

    try:
        frequent_words = most_frequent_words(list_input[1:-1], k)
    except:
        print 'error'
        frequent_words = None

    if frequent_words:
        for word in frequent_words:
            print word

            # To print output to another file
            # if frequent_words:
            # with open('output.txt', 'w') as fp:
            # fp.write('\n'.join(frequent_words))