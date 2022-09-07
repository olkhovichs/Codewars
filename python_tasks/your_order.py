import re

def order(sentence):
    if not sentence:
        return sentence
    else:
        sent_list = sentence.split(' ')
        numbers = re.findall('[1-9]', sentence)
        result = list(dict(sorted((dict(zip(numbers, sent_list))).items())).values())
        return ' '.join(result)
