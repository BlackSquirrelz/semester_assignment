from nltk.tokenize import sent_tokenize as st

class Article:
    kind =  "text"
    
    def __init__(self, issue, article_number, language, title, author, body):
        self.issue = issue
        self.article_number = article_number
        self.language = language
        self.title = title
        self.author = author
        self.body = body

    def stats(self):
        print("Text stats:")

        number_sentences = len(st(self.body))
        print(f"\t number of sentences: {number_sentences}")
