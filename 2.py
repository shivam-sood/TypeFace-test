 
#  Take input from file 2.txt and given word is input_string, find all words in 2.txt which are phonetically similar to input_string using fuzzy search
from fuzzywuzzy import fuzz
input_string = input()
with open('2.txt', 'r') as file:
     input_lines = [line.strip('\n') for line in file]
phonetic_matches = []
for word in input_lines:
    if fuzz.ratio(input_string, word) > 80:
        phonetic_matches.append(word)
print(phonetic_matches)