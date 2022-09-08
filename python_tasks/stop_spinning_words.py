def spin_words(sentence):
    sent_list = sentence.split()
    for i, item in enumerate(sent_list):
        if len(item) >= 5:
            sent_list[i] = item[::-1]
    return ' '.join(sent_list)