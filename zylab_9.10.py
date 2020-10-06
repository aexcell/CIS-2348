# Alexandra Excell PSID: 1595971

# Word frequencies

import csv

file = input()
text = open(file, newline='')
text_lst = list(csv.reader(text,delimiter=','))[0]

text_lst2 = []
word_count =[]
for word in text_lst:
    if word not in text_lst2:
        text_lst2.append(word)
        word_count.append(text_lst.count(word))

for idx in range(0,len(word_count)):
    print(text_lst2[idx],word_count[idx])