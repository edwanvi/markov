import random
import re

#comments. I DID THIS AT A CLASS OKAY
#read wonderland.txt

txt_file = open("C:\Users\c-60981\Documents\wonderland.txt", 'r')

raw_text = txt_file.read()
txt_file.close()

#formatting
text = re.sub('[^a-zA-Z\s]', '', raw_text).lower()
print(text)