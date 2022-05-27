'''

Example:
("abcdefghij", 1) -> "bdfhjacegi"
("abcdefghij", 2) -> "bdfhjacegi" -> "dhaeibfjcg"

'''


def encrypt(text: str, n: int):

    if text == '':
        return text
    if text is None:
        return text
    if (n == '') or (int(n) <= 0):
        return text

    raw_string = text
    arr_len = len(raw_string)
    arr_of_even = []
    arr_of_uneven = []
    n = int(n)

    for elem in range(arr_len):

        if elem % 2 == 0:
            arr_of_even.append(raw_string[elem])
        else:
            arr_of_uneven.append(raw_string[elem])

    result = ''.join(arr_of_uneven + arr_of_even)

    if n > 1:
        return encrypt(result, n - 1)
    return result


text = input('Type your message: ')
n = input('Type n param: ')

print(encrypt(text, n))
