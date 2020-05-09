from nltk.tokenize import sent_tokenize as st

class Article:
    kind =  "text"
    
    def __init__(self, text, lang):
        self.text = text
        self.language = lang

    def stats(self):
        print("Text stats:")

        number_sentences = len(st(self.text))
        print(f"\t number of sentences: {number_sentences}")
