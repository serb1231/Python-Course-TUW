def get_char_bigrams(a):
    dictionar = dict([])
    for i in range(len(a)-1):
        bix = a[i]+a[i+1]
        #print(bix)
        if bix in dictionar:
            dictionar[bix]+=1
        else:
            dictionar.update({bix:1})
    print(dictionar)
    return dictionar

assert get_char_bigrams("apple") == {"ap": 1, "pp": 1, "pl": 1, "le": 1}
assert get_char_bigrams("apple apple") == {
            "ap": 2,
                "pp": 2,
                    "pl": 2,
                        "le": 2,
                            "e ": 1,
                                " a": 1,
                                }
