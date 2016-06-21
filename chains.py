import random
import re

#read wonderland.txt
txt_file = open("C:\Users\c-60981\Downloads\markov-master\wonderland.txt", 'r')
raw_text = txt_file.read()
txt_file.close()

#formatting
text = re.sub('[^a-zA-Z\s]', '', raw_text).lower()
words = text.split()

#store occurences of a unique word after another word
model = {}
for i in range(len(words) - 2):
    #word = words[i]
    pair = words [i] + ',' + words[i + 1]
    if pair not in model:
        model[pair] = {}
    node = model[pair]
    next_word = words[i + 2]
    if next_word not in node:
        node[next_word] = 0
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
    for i in range(length):
        node = model[pair[0] + ',' + pair[1]]
        word = spinner(node)
        sentence += ' ' + word
        pair = [pair[1], word]
    print(sentence)
generateText()
