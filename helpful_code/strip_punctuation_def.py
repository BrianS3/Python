def strip_punctuation(str_w_punc):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    no_punct = ""
    for char in str_w_punc:
        if char not in punctuation_chars:
            no_punct = no_punct+char
    return no_punct
