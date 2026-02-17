def verse(number: int) -> str:
    """Generate the lyrics for a single verse of the beer song.

    :param number: The number of bottles in the verse.
    :return: The lyrics for the verse.
    """
    if number > 2:
        return (
            f"{number} bottles of beer on the wall, {number} bottles of beer."
            "\n"
            f"Take one down and pass it around, "
            f"{number - 1} bottles of beer on the wall."
            "\n"
        )
    elif number == 2:
        return (
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, "
            "1 bottle of beer on the wall.\n"
        )
    elif number == 1:
        return (
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, "
            "no more bottles of beer on the wall.\n"
        )
    else:  # number == 0
        return (
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, "
            "99 bottles of beer on the wall.\n"
        )

def song(start: int = 99, end: int = 0) -> str:
    """Generate the lyrics for the beer song.

    :param start: The number of bottles to start with.
    :param end: The number of bottles to end with (inclusive).
    :return: The lyrics for the beer song.
    """
    verses = []
    for i in range(start, end - 1, -1):
        verses.append(verse(i))
    
    # Join with newlines and ensure exactly two newlines at the end
    return "\n".join(verses)