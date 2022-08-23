import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def something_something():
    user_input = input("Give a word")
    try:
        new_user_list = [nato_alphabet_dict[item] for item in user_input.upper()]
    except KeyError:
        print("Sorry, only letters in alphabet :]")
        something_something()
    else:
        print(new_user_list)


something_something()
