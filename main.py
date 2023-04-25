import requests

try:
    open('./bible.txt', 'r')
except:
    print("Loading...")
    bible = requests.get("https://www.o-bible.com/download/kjv.txt").text
    with open('./bible.txt', 'w') as file_handle:
        file_handle.write(bible)

sentence = input("Are your words in the bible? \n")


with open('./bible.txt', 'r') as bible_handle:
    bible_versets = [verset.split() for verset in bible_handle.readlines()[1:]]
    bible_words = []
    for verset in bible_versets:
        bible_words.extend([word.lower() for word in verset])


ok = False

for word in sentence.split():
    if word.lower() in bible_words:
        ok = True
        print(f'"{word}" is in the bible!')
    
if not ok:
    print("None of those words are in the bible")