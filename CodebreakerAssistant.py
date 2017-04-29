import pickle

infile = 'wordsEnDictPickle.txt'
infile = open(infile, 'rb')
ENGLISH_WORD_DICT = pickle.load(infile)
infile.close()


def word_to_template(word):
    """Converts a word to a different set of letters representing the letter
    occurences in the word"""
    word = word.upper()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word_letters = []
    for letter in word:
        if not letter in word_letters:
            word_letters.append(letter)
    
    for i in range(len(word_letters)):
        word = word.replace(word_letters[i], alphabet[i])
    
    return word

    
def find_fitting_words(given_template):
    converted_word = word_to_template(given_template)
    possible_words = ENGLISH_WORD_DICT.get(converted_word, [])
    word_length = len(given_template)
    resulting_words = []
    for word in possible_words:
        still_possible = True
        for character_index in range(word_length):
            template_char = given_template[character_index]
            possible_word_char = word[character_index]
            if template_char.isalpha() and not template_char == possible_word_char:
                still_possible = False
                break
        if still_possible:
            resulting_words.append(word)    
    
    return resulting_words
    
    
def main():
    given_template = input("Please enter a template or 'Q' to quit: ").lower()
    
    if not(given_template == 'q'):    
        print(find_fitting_words(given_template))
        main()
    
    
if __name__ == '__main__':
    main()

    