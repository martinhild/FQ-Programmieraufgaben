
def _clean_isbn(isbn):
    return isbn.replace("-", "").replace(" ", "")

def _check_if_isbn_10(isbn):
    """ returns True if isbn is a valid isbn10"""
    isbn = _clean_isbn(isbn)
    if len(isbn) != 10:
        return False
    if not isbn[:9].isdigit():
        return False
    if isbn[9] not in "0123456789X":
        return False

    # calculate check digit
    weighted_sum = 0
    for i in range(9):
        n = int(isbn[i])
        weighted_sum += (i+1)*n
    check_digit = weighted_sum % 11

    if isbn[9] in "xX" and check_digit == 10:
        return True
    elif int(isbn[9]) == check_digit:
        return True
    else:
        return False

def _check_if_isbn_13(isbn):
    """ returns True if isbn is a valid isbn13 """
    isbn = _clean_isbn(isbn)
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False

    # calculate check digit
    weighted_sum = 0
    for i in range(12):
        n = int(isbn[i])
        if i % 2 == 0:
            weighted_sum += n
        else:
            weighted_sum += 3 * n
    check_digit = (10 - weighted_sum % 10) % 10

    if check_digit == int(isbn[12]):
        return True
    else:
        return False

def _check_isbn(isbn):
    isbn = _clean_isbn(isbn)
    if len(isbn) == 10:
        valid = _check_if_isbn_10(isbn)
    elif len(isbn) == 13:
        valid = _check_if_isbn_13(isbn)
    else:
        valid = False
    return valid


def main():
    user_input = input("ISBN: ")
    valid = _check_isbn(user_input)
    print("VALID :)" if valid else "INVALID :(")


if __name__=="__main__":
    main()