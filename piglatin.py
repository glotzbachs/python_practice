# turn english to pig latin

# get sentence from user
user_sentence = input('What sentence would you like translated into pig latin?: ').strip().lower()


# split sentence into a list of words

words = user_sentence.split()

# loop through words and convert

converted_words = []

for word in words:
    if word[0] in 'aeiou':
        converted_word = word + 'yay'
        converted_words.append(converted_word)
    else:
        position = 0
        for letter in word:
            if letter not in 'aeiou':
                position += 1
            else:
                break
        consonants = word[:position]
        new_beginning = word[position:]
        converted_word = new_beginning + consonants + 'ay'
        converted_words.append(converted_word)

# put converted words back into sentence

translated_sentence = " ".join(converted_words)

# output!

print(translated_sentence)
