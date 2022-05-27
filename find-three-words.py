

def find_three_words(text: str):

    def symbols_of_ascii():
        '''
        Return list of ASCII characters in the ranges
        33 - 47 | 58 - 64 | 91 - 96 | 123 - 126
        '.', ',', ':', '!', '"', "'", '[', ']', '-', '(', ')', etc.
        '''
        list = []
        list.extend([chr(i) for i in range(33, 48)])
        list.extend([chr(i) for i in range(58, 65)])
        list.extend([chr(i) for i in range(91, 97)])
        list.extend([chr(i) for i in range(123, 127)])
        return list

    lst_no = symbols_of_ascii()
    lst = []

    for word in text.lower().split():
        if not word in lst_no:
            _word = word
            if word[-1] in lst_no:
                _word = _word[:-1]
            if word[0] in lst_no:
                _word = _word[1:]
            lst.append(_word)

    if len(lst) < 3:
        return []

    _dict = dict()
    for word in lst:
        _dict[word] = _dict.get(word, 0) + 1

    _list = []
    for key, value in _dict.items():
        _list.append((value, key))
        _list.sort(reverse=True)

    result = []
    for freq, word in _list[0:3]:
        result.append(word)

    return result


text = input('Type your text: ')
print(find_three_words(text))
