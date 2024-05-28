
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words
result1 = single_root_words('кот', 'котик', 'собака', 'котенок', 'слон', 'котятя')
result2 = single_root_words("дом", "кот", "собака", "дерево", "домик")
print(result1)
print(result2)
