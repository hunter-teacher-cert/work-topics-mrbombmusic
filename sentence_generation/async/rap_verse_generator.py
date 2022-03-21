# hat-tip to Liam Baum and Andrew Healey, a British software engineer, who have both implemented Markov Chains in ways that proved invaluable to our group!
# You can find Liam's (super awesome) lyric generator here on his repo: https://github.com/hunter-teacher-cert/work_csci70900-mrbombmusic/tree/master/ds/markov
# And Healey Codes version here: https://github.com/healeycodes/markov-chain-generator

import random

# This function handles input by opening a file and returning it as a string
def input(text):
    with open(text) as f:
        corpus = f.read()
    return corpus

def build_markov(corpus, state_size):
    corpus = corpus.split()#split the string input into a list of words
    markov = {}#create an empty dictionary to hold the model - keys and values are words
    for i in range(state_size, len(corpus)):
        current_word = corpus[i]
        previous_words = ' '.join(corpus[i-state_size:i])
        if previous_words in markov:
            markov[previous_words].append(current_word)
        else:
            markov[previous_words] = [current_word]
    return markov

def build_rhymes(corpus):
    corpus = corpus.splitlines();
    rhymes = {}
    for i in range(0, len(corpus), 2):
        if i + 1 < len(corpus):
            firstline = corpus[i]
            secondline = corpus[i + 1]
            rhyme1 = firstline.rsplit(' ', 2)[1]
            rhyme1 = rhyme1 + " " + firstline.rsplit(' ', 2)[2]
            rhyme2 = secondline.rsplit(' ', 2)[1]
            rhyme2 = rhyme2 + " " + secondline.rsplit(' ', 2)[2]
            if rhyme1 in rhymes:
                rhymes[rhyme1].append(rhyme2)
            else:
                rhymes[rhyme1] = [rhyme2]
    return rhymes


def generate_line(model, rhymes, state_size, word=None):
    def get_new_starter():
        return random.choice([s.split(' ') for s in model.keys() if s[0].isupper()])
    line = get_new_starter() #starting word
    i = state_size
    while len(line) < 6:
        key = ' '.join(line[i-state_size:i])
        if key not in model:
            text += get_new_starter()
            i += 1
            continue
        next_word = random.choice(model[key])
        line.append(next_word)
        i += 1
    key = ' '.join(line[i-state_size:i])

    next_word = random.choice(model[key])
    if word:
        rhyming_word = random.choice(rhymes[word])
        line.append(rhyming_word)
        pass
    else:
        if next_word not in rhymes:
            next_word = random.choice(list(rhymes.keys()))
            line.append(next_word)
        else:
            line.append(next_word)
            pass
    return ' '.join(line)

def generate_cuplet(line, model, rhymes, state_size):
    rhyming_word = line.rsplit(" ", 2)[1]
    rhyming_word = rhyming_word + " " + line.rsplit(" ", 2)[2]
    second_line = generate_line(model, rhymes, state_size, rhyming_word)
    cuplet = line + '\n' + second_line + '\n'
    return cuplet

def spit_verse(model, rhymes, bars, state_size):
    count = 0
    verse = ""
    while True:
        line = generate_line(model, rhymes, state_size)
        count += 1
        cuplet = generate_cuplet(line, model, rhymes, state_size)
        count += 1
        verse = verse + cuplet
        if count == bars:
            break
    return verse
# This is like "main" in java - here is where we run the program by calling the functions
if __name__ == "__main__":
    body = input('doom.txt')
    model = build_markov(body,1)
    rhymes = build_rhymes(body)
    # print(rhymes)
    print(spit_verse(model, rhymes, 16, 1))
