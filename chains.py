import random
import re

#read wonderland.txt
txt_file = open("wonderland.txt", 'r')
raw_text = txt_file.read()
txt_file.close()

#formatting
text = re.sub('[^a-zA-Z\s]', '', raw_text).lower()
words = text.split()

#where we store occurences of a unique word after another word
model = {}
# run for every word in the text minus two
for i in range(len(words) - 2):
    # pair = word at current index + , + word after current index
    pair = words [i] + ',' + words[i + 1]
    # print("Current pair: " + pair)
    # ^that was dumb
    # if the pair is NOT in our tree, add it
    if pair not in model:
        model[pair] = {}
    # node = model[pair] = current pair
    node = model[pair]
    #next_word = word at index + 2
    next_word = words[i + 2]
    if next_word not in node:
        # create a node for the next word with a 0 count
        node[next_word] = 0
    # add one to our count, increasing the odds for that word to be picked
    node[next_word] += 1

# convert counts to probability
for pair in model:
    node = model[pair]
    total = 0
    for next_word in node:
        total += node[next_word]
    for next_word in node:
        node[next_word] = node[next_word] / float(total)
        
def spinner(node):
    spin = random.random()
    angle = 0
    for next_word in node:
        angle += node[next_word]
        if spin <= angle:
            return next_word
            
def generateText():
    pair = random.choice(model.keys()).split(',')
    sentence = pair[0] + ' ' + pair[1]
    length = 20
    #do it 20 times
    for i in range(length):
        node = model[pair[0] + ',' + pair[1]]
        word = spinner(node)
        #append a space and our new word to the sentence
        sentence += ' ' + word
        pair = [pair[1], word]
    print(sentence)
generateText()
