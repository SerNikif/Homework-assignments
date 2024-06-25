def single_root_words(root_word, *other_words):
    same_words = []
    root_word = str(root_word).lower()
    for i in other_words:
        word = str(i).lower()
        if root_word in word or word in root_word:
            same_words.append(i)

    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

