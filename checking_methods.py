def check_empty_places(word_user_solution):
    for c in word_user_solution:
        if c=='_':
            return True
    return False

def letter_used_multiple_times(used_letters,letter):
    if letter in used_letters:
        return True
    return False

def isfloat(character):
    try:
        float(character)
        return True
    except ValueError:
        return False

def username_exists(username,players):
    if username in players:
        return True
    return False