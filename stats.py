from collections import Counter
def get_num_words(text):
    count = text.split()
    return len(count)

def get_char_count(text):
    LC_text = text.lower()
    chars = {}
    for ch in LC_text:
        if ch in chars:
            chars[ch] += 1
        else: 
            chars[ch] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort(chars):
    newList = []
    for char in chars:
        newList.append({"char": char, "num": chars[char]})
    newList.sort(reverse=True, key=sort_on)
    return newList
