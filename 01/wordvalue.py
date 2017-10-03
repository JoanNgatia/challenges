from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list."""
    f = open(DICTIONARY, 'r')
    new_list = f.read().splitlines()
    return new_list


def calc_word_value(word):
    """
    Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES.
    """
    y = (LETTER_SCORES.get(char.upper(), 0) for char in word)
    return sum(y)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY."""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)


if __name__ == "__main__":
    # run unittests to validate
    print calc_word_value('bob')
