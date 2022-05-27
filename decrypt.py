'''

Example:
("bdfhjacegi", 1) -> "abcdefghij"
("dhaeibfjcg", 2) -> "bdfhjacegi" -> "abcdefghij"

'''


def decrypt(encrypted_text: list, n: int):

    # arr_temp_1 = []
    # arr_temp_2 = []
    encrypted_text = list(encrypted_text)
    text_len = len(encrypted_text)

    if text_len % 2 == 0:
        half_of_text_len = int(text_len / 2)
    else:
        half_of_text_len = int((text_len / 2) + 1)

    result = ''
    i = 0
    n = int(n)

    try:
        while i <= half_of_text_len:
            result += ''.join(encrypted_text[half_of_text_len + i])
            if i == half_of_text_len:
                return result
            else:
                result += ''.join(encrypted_text[0 + i])
            i += 1
        return result
    except IndexError:
        return result
    finally:
        if n > 1:
            return decrypt(result, n - 1)
        return result


encrypted_text = input('Type your encrypted message: ')
n = input('Type n param: ')
print(decrypt(encrypted_text, n))
