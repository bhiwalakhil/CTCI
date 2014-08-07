__author__ = 'akhilbhiwal'




# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
# words = open("words-list.rtf").read().split()
# wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
# maxword = max(len(x) for x in words)
#
# def infer_spaces(s):
# """Uses dynamic programming to infer the location of spaces in a string
# without spaces."""
#
# # Find the best match for the i first characters, assuming cost has
# # been built for the i-1 first characters.
#     # Returns a pair (match_cost, match_length).
#     def best_match(i):
#         candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
#         return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)
#
#     # Build the cost array.
#     cost = [0]
#     for i in range(1,len(s)+1):
#         c,k = best_match(i)
#         cost.append(c)
#
#     # Backtrack to recover the minimal-cost string.
#     out = []
#     i = len(s)
#     while i>0:
#         c,k = best_match(i)
#         assert c == cost[i]
#         out.append(s[i-k:i])
#         i -= k
#
#     return " ".join(reversed(out))

def find_words(instring, prefix='', words=None):
    if not instring:
        return []
    if words is None:
        words = set()
        with open('/usr/share/dict/words') as f:
            for line in f:
                words.add(line.strip())
    if (not prefix) and (instring in words):
        return [instring]
    prefix, suffix = prefix + instring[0], instring[1:]
    solutions = []
    # Case 1: prefix in solution
    if prefix in words:
        try:
            solutions.append([prefix] + find_words(suffix, '', words))
        except ValueError:
            pass
    # Case 2: prefix not in solution
    try:
        solutions.append(find_words(suffix, prefix, words))
    except ValueError:
        pass
    if solutions:
        return sorted(solutions,
                      key=lambda solution: [len(word) for word in solution],
                      reverse=True)[0]
    else:
        raise ValueError('no solution')


# print(find_words('thepanelisalsoexpectedtorecommendthatthewhitehouse'))
# print(find_words('tableapplechairtablecupboard'))
# print(find_words('tableprechaun', words = set(['tab', 'table', 'leprechaun'])))

def stringToDict(string):
    string_dict = {}
    for ch in string:
        if ch not in string_dict:
            string_dict[ch] = 1
        else:
            string_dict[ch] += 1
    return string_dict


def isStringSubset(word, string_dict):
    word_dict = stringToDict(word)
    for key in word_dict.keys():
        if word_dict[key] > string_dict.get(key):
            return False
    return True


if __name__ == '__main__':
    text = """
            thepanelisalsoexpectedtorecommendthatthewhitehouse
            theiraniangovernmenthasmaintainedthatitknowsnothin
            bymatchingthelowestpriceandenhancingservicehewasde
            thisfallherneighborhoodinthenortheasternpartofthis
            forcollegebasketballfansthisisasgoodaweekasyourego
            butaccordingtobarbershopproprietorsthenumberoffema
            anintriguingnewstudysuggeststhatwhatreallydrawspeo
            alsoonthursdaythelatestwinnersofthelifesciencesand
            whatmembersofbothpartiesbemoanedmorethananythingwa
            onekeyhurdleforteslainproducingthenewsmallercarwil
        """
    jumbledText = """
            heeemirhcletshlohttwhsnpuesecetottipoenadeamtoaexd
            tnreaaahninsnootottnhiaihkvnnhimttwmtieadnrisegena
            raomnnaytihhgchawbsindcasveedreeipeeenngcethcltswi
            rrginhnhrllteantfttpaiashneshoeiehrbettshofodiroho
            eaerigtolelyeaarufakoglceesoifwsolsbshsdgoosnkbata
            nebtrdpueroribgffbhmsmcaeutaoseprrerprttoocioonbah
            aawituendgiriygswarlaernplnotseghydtssttwathgenusu
            eotsruilahtnridseaicennoasadnefwhteeenfltcostyslhs
            aeoaaebhabmtrnoniwtarwetgnfamthsoryhoedemhmnebspti
            mgreironluhrdleraowlniykwafluisreaeecdtehcenpolstn
        """

    string = 'heeemirhcletshlohttwhsnpuesecetottipoenadeamtoaexd'
    string_dict = stringToDict(string)

    words = set()
    with open('/usr/share/dict/words') as f:
        for line in f:
            words.add(line.strip())

    possible_words = []
    for word in words:
        if isStringSubset(word, string_dict):
            possible_words.append(word)

    possible_words2 = possible_words[:]

    possible_words_set = set()
    for word in possible_words:
        orig_word = word
        word = ''.join(sorted(word))
        if word not in possible_words_set:
            possible_words_set.add(word)
        else:
            possible_words2.remove(orig_word)

    print len(possible_words2), len(possible_words), len(possible_words_set)