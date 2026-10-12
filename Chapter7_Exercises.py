import doctest


# --------------------------------------------------
# Exercise 7.9.1 - Explain the early-return mistake
# --------------------------------------------------
# If return False is inside the for loop's else block, Python stops
# as soon as the FIRST letter does not match. That means a later
# matching letter never gets checked. The final return False needs
# to be OUTSIDE the loop so every letter can be examined first.


def uses_any(word, letters):
    """Check if a word has any of the given letters.

    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    >>> uses_any('Banana', 'AEIOU')
    True
    """
    letters = letters.lower()
    for letter in word.lower():
        if letter in letters:
            return True
    return False


# --------------------------------------------------
# Exercise 7.9.2 - Avoid all forbidden letters
# --------------------------------------------------

def uses_none(word, forbidden):
    """Return True when the word avoids every forbidden letter.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    >>> uses_none('BANANA', 'A')
    False
    """
    forbidden = forbidden.lower()
    for letter in word.lower():
        if letter in forbidden:
            return False
    return True


# --------------------------------------------------
# Exercise 7.9.3 - Use only the available letters
# --------------------------------------------------

def uses_only(word, available):
    """Return True when every letter in word is available.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('BANANA', 'ban')
    True
    >>> uses_only('', 'abc')
    True
    """
    available = available.lower()
    for letter in word.lower():
        if letter not in available:
            return False
    return True


# --------------------------------------------------
# Exercise 7.9.4 - Include every required letter
# --------------------------------------------------

def uses_all(word, required):
    """Return True when word includes all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('BANANA', 'NaB')
    True
    >>> uses_all('banana', 'nnbaa')
    True
    """
    word = word.lower()
    for letter in required.lower():
        if letter not in word:
            return False
    return True


# --------------------------------------------------
# Exercise 7.9.5 - Spelling Bee word check and score
# --------------------------------------------------

def check_word(word, available, required):
    """Check a word against the Spelling Bee letter rules.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    >>> check_word('CART', 'ACDLORT', 'R')
    True
    """
    if len(word) < 4:
        return False
    if not uses_only(word, available):
        return False
    if not uses_all(word, required):
        return False
    return True


def word_score(word, available):
    """Score a valid Spelling Bee word, including pangram bonus.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    >>> word_score('cart', 'ACDLORT')
    1
    """
    if len(word) == 4:
        points = 1
    else:
        points = len(word)

    if uses_all(word, available):
        points += 7
    return points


# --------------------------------------------------
# Exercise 7.9.6 - Reuse an existing function
# --------------------------------------------------

def uses_none_with_any(word, forbidden):
    """Another uses_none, written by reusing uses_any.

    >>> uses_none_with_any('banana', 'xyz')
    True
    >>> uses_none_with_any('apple', 'efg')
    False
    >>> uses_none_with_any('', 'abc')
    True
    """
    return not uses_any(word, forbidden)


# --------------------------------------------------
# Exercise 7.9.7 - Reuse uses_only to create uses_all
# --------------------------------------------------

def uses_all_with_only(word, required):
    """Check all required letters by swapping uses_only arguments.

    >>> uses_all_with_only('banana', 'ban')
    True
    >>> uses_all_with_only('apple', 'api')
    False
    >>> uses_all_with_only('banana', 'nnbaa')
    True
    """
    return uses_only(required, word)


# --------------------------------------------------
# Exercise 7.9.8 - Reuse uses_any to create uses_all
# --------------------------------------------------

def uses_all_with_any(word, required):
    """Check each required character by calling uses_any.

    >>> uses_all_with_any('banana', 'ban')
    True
    >>> uses_all_with_any('apple', 'api')
    False
    >>> uses_all_with_any('banana', 'nnbaa')
    True
    """
    for letter in required:
        if not uses_any(word, letter):
            return False
    return True


# --------------------------------------------------
# Run doctests and a few easy-to-read examples
# --------------------------------------------------
if __name__ == '__main__':
    results = doctest.testmod()
    print(f'Doctests run: {results.attempted}')
    print(f'Doctests failed: {results.failed}')
    print()
    print('Spelling Bee examples:')
    available_letters = 'ACDLORT'
    required_letter = 'R'
    for word in ('color', 'ratatat', 'rat', 'told', 'bee', 'card', 'cartload'):
        accepted = check_word(word, available_letters, required_letter)
        if accepted:
            print(f'{word}: accepted, {word_score(word, available_letters)} point(s)')
        else:
            print(f'{word}: not accepted')
