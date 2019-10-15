def hamming_distance(string1, string2):
    '''
        Algorithm : Hamming Distance

        Desc : the Hamming distance between two strings of equal length is the
               number of positions at which the corresponding symbols are
               different

        Warning : if str1 and str2 length is not equal the func returns int(0)
    '''

    hamming_distance = 0

    if len(string1) != len(string2):
        return 0  # see Warning! on __doc__
    else:
        for i in range(0, len(string1), 1):
            if string1[i] == string2[i]:
                continue  # do nothing
            elif string1[i] != string2[i]:
                hamming_distance += 1
        return hamming_distance
