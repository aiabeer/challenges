def abbreviate(phrase):
    words = phrase.replace('-', ' ').replace(':', ' ').replace(',', ' ').split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
    