# function will convert string parameter to upper case
def to_upper(string):
    if not isinstance(string, str):
        raise TypeError("Argument must be a string")
    return string.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(word_list):
    if not isinstance(word_list, list):
        raise TypeError("Argument must be a list")
    return all(word.isupper() for word in word_list)