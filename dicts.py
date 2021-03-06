"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # define a function that takes in a string
    test_dict = {}
    # split the string into a list and iterate through it
    for word in phrase.split(' '):
        # if the word not in dictionary, add the word with a value of 1
        if word not in test_dict:
            test_dict[word] = 1
        #if the word is already in the dictionary, add 1 to the value
        else:
            test_dict[word] += 1

    # return the dictionary ({word: numOccurs})
    return test_dict

print(count_words("Apple berry cherry apple banana cherry cherry"))

#--------------------------------------------------------------------------------------------------------------

def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
    # create a dictionary of melons
    melon_dict = {"honeydew": 1.50, "watermelon": 3.75, "musk": 2.25, "cantaloupe": 2.25}
    count = 0
    # iterate through the dictionary
    for key, value in sorted(melon_dict.items()):
        # check to see if the current value matches the price
        if value == price:
            # if it matches, print ou the melon's name
            print(key)
        else:
            count += 1
    # if the count does not equal the length of the dictionary's keys, then a match was found
        # if count does equal the lenght of the dictionary, then no melons match the price
    if count >= len(melon_dict):
        print("None found")    
    

print_melon_at_price(5)
# note for teachers:
    # I wasn't able to figure out a way to prevent "None found" from being printed every time an iteration
        # did not find a matching price. 
        # I know the code above works, but I'd like to know a more elegant solution
#--------------------------------------------------------------------------------------------------------------


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

        # create a dicitonary of english to priate talk
    pirate_dict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    # create an empty list
    pirate_string = []
    # split the string into a list, and iterate through it
    for word in phrase.split(' '):
        # if a word in the phrase matches a key, add the value of the key to the list
        # if it doesn't match, add the word itself to the list
        pirate_string.append(pirate_dict.get(word, word))
    # return the list of words joined into a string
    print(' '.join(pirate_string))
    
translate_to_pirate_talk("This student has an excuse for your professor")
# output: This swabbie has an arr for yer foul blaggart

#--------------------------------------------------------------------------------------------------------------

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

       # create an empty dictionary
    # with for loop, populate dictionary where the key is the name, 
        # and the value is the last character of the previous name
    # create list to return, starting automatically with the first name in the list
    # iterate through keys
        # create a variable that equals the last character of the first name
        # add a key if the name starts with the last character
        # don't add a name if it already has been added
        # update the last character to equal the current key's last character
    
    list_returned = [names[0]]
    poss_dict = {}
    last_char = names[0][-1]

    for index in range(len(names)):
        poss_dict[names[index]] = names[index - 1][-1]
    

    # for key in poss_dict.keys():
    #      if key not in list_returned and key[0] != last_char:
    #         list_returned.append(key)
    #         last_char = key[-1]
        
    for key in poss_dict.keys():
        if key[0] == last_char and key not in list_returned:
            list_returned.append(key)
            last_char = key[-1]

    return list_returned  # ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']


print(kids_game(["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "nicky"]))
# note: I TRIED REALLY HARD!!! I just can't figure it out
