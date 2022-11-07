"""Count words in file."""


# put your code here.
text = open('test.txt')

word_count = {}

all_words = []

for line in text:
    line = line.rstrip()
    words = line.split(' ')
    all_words.extend(words)

for word in all_words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1
#     word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f'{word} {count}')