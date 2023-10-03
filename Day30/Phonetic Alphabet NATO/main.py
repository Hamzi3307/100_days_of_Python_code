import pandas

data = pandas.read_csv("Day30\Phonetic Alphabet NATO\Phonetic Alphabet.csv")

#TODO 1. Create a dictionary from file as
# {letter:code, letter:code, letter:code, ...}
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}
print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        word_input = input("Enter a word: ")
        list_phoned = [phonetic_dict[ltr] for ltr in word_input.upper()]
    except KeyError:
        print('Sorry Only letters in the alphabets')
    else:
        break
print(list_phoned)

