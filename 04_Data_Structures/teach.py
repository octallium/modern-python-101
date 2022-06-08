"""

Set:
----
Louis has graduated from school and now wants to teach Zortans
how to talk in English. But English is complicated, so lets try
to simplify it using Sets.

Set is all about being `unique`, it's very useful for certain operations.

Info:
-----
In a Set all values are unique
"""

# ---------------------------------------------------------------------
# Louis wants to impress by showing some English magic, but Zortans are
# confused, they want him to first shows unique alphabets in his magic.
# ---------------------------------------------------------------------

magic_word = "abracadabra"
unique_alphabets: set[str] = set(magic_word)
print(f"Unique Alphabets: {unique_alphabets}")

sentence = "the big blue sky and the big blue ocean"
unique_alphabets = set(sentence)
print(f"Unique Alphabets: {unique_alphabets}")

# Whats happens if we want to see list of unique words instead of alphabets
word_list = sentence.split()  # split the string into words and save in a list
print(f"Word List: {word_list}")
# extract the unique words
unique_words = set(word_list)
print(f"Unique Words: {unique_words}")

# ---------------------------------------------------------------------
# Zortans are impressed and they want to add more words to the set
# ---------------------------------------------------------------------

unique_words.update(["big", "blue", "sky"])
print(f"Unique Words: {unique_words}")  # Nothing happens!!

unique_words.update(["green", "grass"])
print(f"Unique Words: {unique_words}")  # Something Happens!!

# ---------------------------------------------------------------------
# Zortans don't like the word grass and wants to remove it
# ---------------------------------------------------------------------

unique_words.discard("grass")
print(f"Unique Words: {unique_words}")

"""
Read more about operations such as union, intersection, etc.
"""
